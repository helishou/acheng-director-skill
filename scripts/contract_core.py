"""Small shared primitives for versioned production contracts."""
import hashlib
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ValueError(message)


# Git converts line endings for tracked text on checkout, so a digest recorded on
# one platform would otherwise fail on another. Text files are therefore hashed in
# their canonical LF form. Binary media is identified by extension, never by
# sniffing bytes: a small PNG can contain no NUL, and normalizing it would weaken
# the integrity check that binary media exists to provide.
TEXT_SUFFIXES = frozenset({
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".js", ".mjs", ".ts",
    ".tsx", ".jsx", ".csv", ".toml", ".ini", ".cfg", ".sh", ".bat", ".ps1",
})


def is_text_path(path):
    return Path(path).suffix.lower() in TEXT_SUFFIXES


def canonical_bytes(data):
    """Line-ending-normalized bytes of text content."""
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def bytes_hash(data):
    """sha256 of raw bytes with line endings normalized (for text content)."""
    return hashlib.sha256(canonical_bytes(data)).hexdigest()


def file_hash(path):
    """sha256 of a tracked file: canonical LF for text, raw bytes for binary media."""
    data = Path(path).read_bytes()
    return bytes_hash(data) if is_text_path(path) else hashlib.sha256(data).hexdigest()


def prose(value):
    return isinstance(value, str) and len(value.strip()) >= 3 and value.strip().lower() not in {"unknown", "todo", "tbd", "n/a"}


def indexed(items, label, allow_empty=False):
    need(isinstance(items, list) and (items or allow_empty), f"{label}: list required")
    need(all(isinstance(x, dict) and isinstance(x.get("id"), str) and x["id"].strip() for x in items), f"{label}: object/id required")
    result = {x["id"]: x for x in items}
    need(len(result) == len(items), f"{label}: duplicate id")
    return result


def content_hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":"), allow_nan=False).encode()).hexdigest()
