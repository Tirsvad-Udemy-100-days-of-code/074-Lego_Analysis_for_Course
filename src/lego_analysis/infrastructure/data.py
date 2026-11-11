"""Infrastructure: read the LEGO CSV files into DataFrames."""

from pathlib import Path

import pandas as pd

DATA_DIR: Path = Path(__file__).resolve().parents[3] / "data"


def _read(name: str, data_dir: Path | str | None) -> pd.DataFrame:
    base = DATA_DIR if data_dir is None else Path(data_dir)
    return pd.read_csv(base / name)


def load_colors(data_dir: Path | str | None = None) -> pd.DataFrame:
    """Load colors.csv (id, name, rgb, is_trans)."""
    return _read("colors.csv", data_dir)


def load_sets(data_dir: Path | str | None = None) -> pd.DataFrame:
    """Load sets.csv (set_num, name, year, theme_id, num_parts)."""
    return _read("sets.csv", data_dir)


def load_themes(data_dir: Path | str | None = None) -> pd.DataFrame:
    """Load themes.csv (id, name, parent_id)."""
    return _read("themes.csv", data_dir)
