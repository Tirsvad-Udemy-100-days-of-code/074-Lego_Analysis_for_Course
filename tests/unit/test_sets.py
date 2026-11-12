import pandas as pd

from lego_analysis.application.analysis import (
    count_sets_in_year,
    first_release_year,
    first_sets,
    largest_sets,
)


def test_first_release_year_is_1949(sets: pd.DataFrame) -> None:
    assert first_release_year(sets) == 1949


def test_count_sets_in_1949_is_5(sets: pd.DataFrame) -> None:
    assert count_sets_in_year(sets, 1949) == 5


def test_first_sets_are_all_from_first_year(sets: pd.DataFrame) -> None:
    result = first_sets(sets)

    assert len(result) == 5
    assert set(result["year"]) == {1949}


def test_largest_set_is_bigbox_with_9987_parts(sets: pd.DataFrame) -> None:
    top = largest_sets(sets).iloc[0]

    assert top["set_num"] == "BIGBOX-1"
    assert top["name"] == "The Ultimate Battle for Chima"
    assert top["num_parts"] == 9987


def test_second_largest_set_is_ucs_millennium_falcon(sets: pd.DataFrame) -> None:
    second = largest_sets(sets).iloc[1]

    assert second["name"] == "UCS Millennium Falcon"
    assert second["num_parts"] == 7541


def test_largest_sets_default_returns_five(sets: pd.DataFrame) -> None:
    assert len(largest_sets(sets)) == 5


def test_largest_sets_keeps_input_order_on_ties(small_sets: pd.DataFrame) -> None:
    assert largest_sets(small_sets, 2)["set_num"].tolist() == ["b", "c"]


def test_largest_sets_with_n_above_size_returns_all(small_sets: pd.DataFrame) -> None:
    assert len(largest_sets(small_sets, 99)) == len(small_sets)


def test_count_sets_in_unknown_year_is_zero(small_sets: pd.DataFrame) -> None:
    assert count_sets_in_year(small_sets, 1800) == 0


def test_first_sets_of_small_frame(small_sets: pd.DataFrame) -> None:
    assert first_sets(small_sets)["set_num"].tolist() == ["b", "e"]
