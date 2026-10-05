"""Committed example bundles must equal what the compilers produce today.

The `examples/compiled/**` bundles are committed deliverables that DELIVERY.md links
to. Nothing regenerated them in place, so a prompt-rule change could ship with stale
fixtures and only surface when a user followed a link. This test recompiles every
example into a throwaway temp directory and compares content; on drift it names the
exact files so the bundles can be refreshed instead of hand-compiled into the repo.

Comparison uses the canonical digest, not raw bytes: git converts line endings on
checkout, so a byte comparison would fail on every non-native platform without any
real change. Binary reference media is still compared byte for byte.
"""
import json
from pathlib import Path
import tempfile
import unittest

from audit_storyboard_quality import read_data
from compile_assets import compile_assets
from compile_h3 import compile_package
from contract_core import file_hash

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
COMPILED = EXAMPLES / "compiled"


def bundle_files(directory):
    """Every regular file under `directory`, as repo-relative POSIX paths."""
    return {
        path.relative_to(directory).as_posix()
        for path in directory.rglob("*")
        if path.is_file()
    }


def bundle_digests(directory):
    """Canonical digest per file, so CRLF and LF checkouts compare equal."""
    return {
        path.relative_to(directory).as_posix(): file_hash(path)
        for path in directory.rglob("*")
        if path.is_file()
    }


class CompiledExampleFreshness(unittest.TestCase):
    def test_every_example_recompiles_to_its_committed_bundle(self):
        sources = sorted(EXAMPLES.glob("*.production.json"))
        self.assertTrue(sources, "No example production files found")

        for source in sources:
            folder = source.name.split("-", 1)[1].split(".", 1)[0]
            production = read_data(source)
            # Mirror validate_director_contract: the H3 bundle is a draft bundle only
            # when the example declares missing references, and image references may
            # be planned only when the example ships an asset_plan.
            draft_video = bool(production.get("example_delivery_expectation"))
            draft_images = bool(production.get("asset_plan"))

            with self.subTest(example=folder), tempfile.TemporaryDirectory() as temporary:
                temp = Path(temporary)
                compiled_video = temp / "video"
                compiled_images = temp / "images"
                compile_package(source, compiled_video, draft=draft_video)
                compile_assets(source, compiled_images, allow_missing=draft_images)

                for committed, fresh in ((COMPILED / folder, compiled_video),
                                         (COMPILED / "images" / folder, compiled_images)):
                    label = committed.relative_to(ROOT).as_posix()
                    self.assertTrue(committed.is_dir(), f"Committed bundle missing: {label}")

                    committed_files = bundle_files(committed)
                    fresh_files = bundle_files(fresh)
                    self.assertEqual(
                        committed_files - fresh_files, set(),
                        f"{label} carries files the compiler no longer emits")
                    self.assertEqual(
                        fresh_files - committed_files, set(),
                        f"{label} is stale: recompile to add these files")
                    committed_digests = bundle_digests(committed)
                    fresh_digests = bundle_digests(fresh)
                    differing = sorted(
                        name for name in committed_files & fresh_files
                        if committed_digests[name] != fresh_digests[name]
                    )
                    self.assertEqual(
                        differing, [],
                        f"{label} is stale: recompile to update {len(differing)} file(s)")


if __name__ == "__main__":
    unittest.main()