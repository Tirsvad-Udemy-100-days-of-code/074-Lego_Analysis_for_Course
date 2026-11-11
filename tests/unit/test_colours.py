import pandas as pd

from lego_analysis.application.analysis import (
    count_opaque_colours,
    count_transparent_colours,
    count_unique_colours,
    transparent_counts_groupby,
    transparent_counts_value_counts,
)


def test_count_unique_colours_is_135(colors: pd.DataFrame) -> None:
    assert count_unique_colours(colors) == 135


def test_transparent_counts_groupby_matches_data(colors: pd.DataFrame) -> None:
    assert transparent_counts_groupby(colors) == {"f": 107, "t": 28}


def test_transparent_counts_methods_agree(colors: pd.DataFrame) -> None:
    assert transparent_counts_groupby(colors) == transparent_counts_value_counts(colors)


def test_opaque_and_transparent_counts_match_dict(colors: pd.DataFrame) -> None:
    assert count_opaque_colours(colors) == 107
    assert count_transparent_colours(colors) == 28


def test_count_unique_colours_ignores_duplicate_names() -> None:
    frame = pd.DataFrame({"name": ["Red", "Red", "Blue"]})

    assert count_unique_colours(frame) == 2


def test_transparent_counts_omit_missing_flag() -> None:
    frame = pd.DataFrame({"id": [1, 2], "is_trans": ["f", "f"]})

    assert transparent_counts_groupby(frame) == {"f": 2}
    assert transparent_counts_value_counts(frame) == {"f": 2}
    assert count_transparent_colours(frame) == 0


def test_counts_on_empty_frame_are_zero() -> None:
    frame = pd.DataFrame({"id": [], "name": [], "is_trans": []})

    assert count_unique_colours(frame) == 0
    assert transparent_counts_groupby(frame) == {}
    assert count_opaque_colours(frame) == 0
