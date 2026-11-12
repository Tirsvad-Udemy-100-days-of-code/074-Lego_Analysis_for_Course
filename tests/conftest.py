"""Shared fixtures: the real data set and small hand-made frames."""

import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")

from lego_analysis.infrastructure.data import load_colors, load_sets, load_themes  # noqa: E402


@pytest.fixture(scope="session")
def colors() -> pd.DataFrame:
    return load_colors()


@pytest.fixture(scope="session")
def sets() -> pd.DataFrame:
    return load_sets()


@pytest.fixture(scope="session")
def themes() -> pd.DataFrame:
    return load_themes()


@pytest.fixture
def small_sets() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "set_num": ["a", "b", "c", "d", "e"],
            "name": ["A", "B", "C", "D", "E"],
            "year": [2000, 1999, 2000, 2001, 1999],
            "theme_id": [1, 1, 2, 2, 2],
            "num_parts": [10, 50, 50, 5, 7],
        }
    )


@pytest.fixture
def small_themes() -> pd.DataFrame:
    return pd.DataFrame(
        {"id": [1, 2, 3], "name": ["One", "Two", "One"], "parent_id": [None, 1, 1]}
    )
