import pandas as pd

from lego_analysis.application.analysis import (
    drop_incomplete_years,
    parts_per_set,
    sets_by_year,
    themes_by_year,
)


def test_sets_by_year_counts_1949(sets: pd.DataFrame) -> None:
    assert sets_by_year(sets).loc[1949, "set_num"] == 5


def test_sets_by_year_counts_2019(sets: pd.DataFrame) -> None:
    assert sets_by_year(sets).loc[2019, "set_num"] == 840


def test_sets_by_year_exposes_set_num_attribute(sets: pd.DataFrame) -> None:
    assert sets_by_year(sets).set_num.iloc[0] == 5


def test_themes_by_year_has_nr_themes_column(sets: pd.DataFrame) -> None:
    result = themes_by_year(sets)

    assert list(result.columns) == ["nr_themes"]
    assert result.index.name == "year"


def test_themes_by_year_counts_distinct_themes(small_sets: pd.DataFrame) -> None:
    result = themes_by_year(small_sets)

    assert result["nr_themes"].to_dict() == {1999: 2, 2000: 2, 2001: 1}


def test_parts_per_set_is_mean_per_year(small_sets: pd.DataFrame) -> None:
    result = parts_per_set(small_sets)

    assert result["num_parts"].to_dict() == {1999: 28.5, 2000: 30.0, 2001: 5.0}


def test_drop_incomplete_years_removes_two_rows(sets: pd.DataFrame) -> None:
    per_year = sets_by_year(sets)

    assert len(drop_incomplete_years(per_year)) == len(per_year) - 2


def test_drop_incomplete_years_removes_the_last_years(sets: pd.DataFrame) -> None:
    per_year = sets_by_year(sets)

    assert drop_incomplete_years(per_year).index[-1] == per_year.index[-3]


def test_drop_incomplete_years_honours_custom_n(small_sets: pd.DataFrame) -> None:
    assert len(drop_incomplete_years(parts_per_set(small_sets), n=1)) == 2


def test_drop_incomplete_years_with_zero_keeps_everything(
    small_sets: pd.DataFrame,
) -> None:
    frame = parts_per_set(small_sets)

    assert len(drop_incomplete_years(frame, n=0)) == len(frame)


def test_drop_incomplete_years_on_short_frame_gives_empty() -> None:
    frame = pd.DataFrame({"x": [1, 2]})

    assert drop_incomplete_years(frame).empty
