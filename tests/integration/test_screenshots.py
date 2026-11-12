"""Integration test: the screenshot script writes the nine step images."""

import importlib.util
from pathlib import Path
from types import ModuleType

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "make_screenshots.py"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_NAMES = {
    "step-1-colours.png",
    "step-2-sets.png",
    "step-3-sets-per-year.png",
    "step-4-themes-per-year.png",
    "step-5-two-axes.png",
    "step-6-parts-per-set.png",
    "step-7-themes-and-keys.png",
    "step-8-merge.png",
    "step-9-bar-chart.png",
}


def _load_script() -> ModuleType:
    """Import scripts/make_screenshots.py by file path."""
    spec = importlib.util.spec_from_file_location("make_screenshots", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_main_writes_nine_valid_png_files(tmp_path: Path) -> None:
    """Each expected image exists, is non-empty and has the PNG signature."""
    _load_script().main(tmp_path)

    files = sorted(tmp_path.glob("*.png"))
    assert {file.name for file in files} == EXPECTED_NAMES
    assert len(files) == 9
    for file in files:
        data = file.read_bytes()
        assert data
        assert data.startswith(PNG_SIGNATURE)
