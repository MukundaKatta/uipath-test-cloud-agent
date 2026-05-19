"""Smoke tests that exercise the package layout without requiring UiPath Labs access.

These intentionally fail loudly the moment the package layout drifts so the
next agent (or future me) catches it before the build pipeline does.
"""

from __future__ import annotations


def test_package_layout_exists() -> None:
    """The Coded Agent source tree must be importable as `src` once added."""
    import pathlib

    root = pathlib.Path(__file__).parent.parent
    assert (root / "src").is_dir(), "src/ tree is missing"
    assert (root / "submissions" / "uipath-agenthack.md").is_file(), (
        "Devpost submission draft is missing"
    )
    assert (root / "docs" / "video-script.md").is_file(), (
        "Demo video script is missing"
    )
