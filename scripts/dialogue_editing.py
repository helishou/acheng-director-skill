"""Compile camera coverage from authored dialogue timing without changing the Shot timeline."""
from fractions import Fraction


def _rows(value):
    return value if isinstance(value, list) else []


def _character_for(line, production):
    characters = _rows(production.get("character_registry"))
    explicit = line.get("character_id")
    if explicit and any(character.get("id") == explicit for character in characters):
        return next(character for character in characters if character.get("id") == explicit)
    bindings = production.get("prompt_bindings", {})
    return next((character for character in characters
                 if line.get("speaker_name") in (character.get("name"), bindings.get(character.get("id")))), None)


def compile_dialogue_camera_guidance(shot, production, referenced_subjects=None):
    """Return model-facing close-up/reverse-shot cues on exact authored local frames."""
    if production.get("prompt_detail_policy", {}).get("profile") == "legacy_fixture":
        return ""
    if shot.get("camera", {}).get("framing") and shot.get("camera", {}).get("editorial_reason"):
        return ""  # Explicit independent views already own their cuts and attention.
    visible = {character.get("id") for character in _rows(shot.get("characters"))}
    listeners = [character for character in _rows(shot.get("characters")) if character.get("id")]
    fps = Fraction(production.get("fps_den", 1), production.get("fps_num", 24))
    references = referenced_subjects or {}
    registered = {character.get("id"): character for character in _rows(production.get("character_registry"))}

    def view_name(character):
        source = registered.get(character.get("id"), {})
        return references.get(character.get("id")) or production.get("prompt_bindings", {}).get(character.get("id")) or source.get("name") or character.get("name") or "the named character"

    def time(frame):
        milliseconds = round(Fraction(frame) * fps * 1000)
        return f"{milliseconds // 60000:02d}:{milliseconds // 1000 % 60:02d}.{milliseconds % 1000:03d}"

    directives = []
    previous_speaker = None
    for line in sorted(_rows(shot.get("dialogues")), key=lambda item: (item.get("start", 0), item.get("end", 0))):
        if line.get("voiceover", False):
            continue
        speaker = _character_for(line, production)
        if not speaker:
            continue
        start, end = line.get("start"), line.get("end")
        if type(start) is not int or type(end) is not int or end <= start:
            continue
        if speaker["id"] in visible:
            if previous_speaker == speaker["id"]:
                directives.append(f"From local shot time {time(start)}, hold the close view on {view_name(speaker)} for the next uninterrupted turn; preserve its authored eyeline and the original acting beat.")
            else:
                directives.append(f"At local shot time {time(start)}, cut on the speaker turn to a close-up of {view_name(speaker)}'s face and shoulders as the active speaker. Preserve the authored screen side, eyeline and action axis; keep the original movement and contact facts unchanged.")
            previous_speaker = speaker["id"]
        else:
            listener = next((item for item in listeners if item.get("id") != speaker["id"]), None)
            if listener:
                directives.append(f"During {time(start)}–{time(end)}, frame {view_name(listener)} in a close reaction view while {view_name(speaker)} speaks from the established offscreen scene position. Keep this diegetic speech distinct from narration; the visible listener remains silent and does not mouth the line.")
            previous_speaker = speaker["id"]

        # A long multi-clause turn can reveal the listener on its final clause.
        # Keep the cut on a natural punctuation boundary and inside the authored speech window.
        text = line.get("text", "")
        clause_marks = [index + 1 for index, char in enumerate(text) if char in "，,；;"]
        listener = next((item for item in listeners if item.get("id") != speaker["id"]), None)
        if listener and len(text) >= 20 and clause_marks:
            split_at = clause_marks[-1]
            ratio = Fraction(split_at, len(text))
            reaction_frame = start + round((end - start) * ratio)
            if start + 10 <= reaction_frame <= end - 10 and len(text) - split_at >= 5:
                directives.append(f"At local shot time {time(reaction_frame)}, on the authored clause break, cut to a close reaction view of {view_name(listener)} as {view_name(speaker)} continues the final clause offscreen. Keep the listener's lips still and preserve the original speaker, words and timing.")

    if not directives:
        return ""
    return "Dialogue-led editorial coverage derived from the immutable speaker and frame schedule: " + " ".join(directives) + " These local camera cuts occur inside the authored Shot and do not alter its duration, action order, global axis or Clip boundaries."
