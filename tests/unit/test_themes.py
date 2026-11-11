import pandas as pd

from lego_analysis.application.analysis import (
    find_theme_ids,
    merge_theme_names,
    set_theme_count,
    sets_for_theme_ids,
    top_themes,
)


def test_star_wars_has_four_theme_ids(themes: pd.DataFrame) -> None:
    assert len(find_theme_ids(themes, "Star Wars")) == 4


def test_find_theme_ids_unknown_name_is_empty(themes: pd.DataFrame) -> None:
    assert find_theme_ids(themes, "No Such Theme") == []


def test_find_theme_ids_returns_all_matches(small_themes: pd.DataFrame) -> None:
    assert find_theme_ids(small_themes, "One") == [1, 3]


def test_sets_for_theme_ids_filters_sets(small_sets: pd.DataFrame) -> None:
    assert sets_for_theme_ids(small_sets, [1])["set_num"].tolist() == ["a", "b"]


def test_sets_for_empty_id_list_is_empty(small_sets: pd.DataFrame) -> None:
    assert sets_for_theme_ids(small_sets, []).empty


def test_set_theme_count_columns_and_order(small_sets: pd.DataFrame) -> None:
    result = set_theme_count(small_sets)

    assert list(result.columns) == ["id", "set_count"]
    assert result["id"].tolist() == [2, 1]
    assert result["set_count"].tolist() == [3, 2]


def test_star_wars_theme_158_has_most_sets(
    sets: pd.DataFrame, themes: pd.DataFrame
) -> None:
    merged = merge_theme_names(set_theme_count(sets), themes)

    first = merged.iloc[0]
    assert first["id"] == 158
    assert first["name"] == "Star Wars"
    assert first["set_count"] == 753


def test_merge_theme_names_keeps_count_order(
    small_sets: pd.DataFrame, small_themes: pd.DataFrame
) -> None:
    merged = merge_theme_names(set_theme_count(small_sets), small_themes)

    assert merged["name"].tolist() == ["Two", "One"]


def test_merge_drops_counts_without_known_theme(small_themes: pd.DataFrame) -> None:
    counts = pd.DataFrame({"id": [9, 1], "set_count": [5, 1]})

    assert merge_theme_names(counts, small_themes)["id"].tolist() == [1]


def test_top_themes_defaults_to_ten(sets: pd.DataFrame, themes: pd.DataFrame) -> None:
    merged = merge_theme_names(set_theme_count(sets), themes)

    assert len(top_themes(merged)) == 10


def test_top_themes_with_fewer_rows_returns_all(
    small_sets: pd.DataFrame, small_themes: pd.DataFrame
) -> None:
    merged = merge_theme_names(set_theme_count(small_sets), small_themes)

    assert len(top_themes(merged, 10)) == 2
