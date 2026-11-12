"""Pure analysis functions on the LEGO DataFrames; no I/O and no plotting."""

import pandas as pd

from lego_analysis.domain.rules import (
    DEFAULT_LARGEST_SETS,
    DEFAULT_TOP_THEMES,
    INCOMPLETE_TRAILING_YEARS,
    OPAQUE_FLAG,
    TRANSPARENT_FLAG,
)


def count_unique_colours(colors: pd.DataFrame) -> int:
    """Return the number of distinct colour names."""
    return int(colors["name"].nunique())


def transparent_counts_groupby(colors: pd.DataFrame) -> dict[str, int]:
    """Count colours per is_trans flag using groupby."""
    counts = colors.groupby("is_trans")["id"].count()
    return {str(flag): int(n) for flag, n in counts.items()}


def transparent_counts_value_counts(colors: pd.DataFrame) -> dict[str, int]:
    """Count colours per is_trans flag using value_counts."""
    counts = colors["is_trans"].value_counts().sort_index()
    return {str(flag): int(n) for flag, n in counts.items()}


def count_transparent_colours(colors: pd.DataFrame) -> int:
    """Return how many colours are transparent."""
    return int((colors["is_trans"] == TRANSPARENT_FLAG).sum())


def count_opaque_colours(colors: pd.DataFrame) -> int:
    """Return how many colours are opaque."""
    return int((colors["is_trans"] == OPAQUE_FLAG).sum())


def first_release_year(sets: pd.DataFrame) -> int:
    """Return the earliest release year."""
    return int(sets["year"].min())


def first_sets(sets: pd.DataFrame) -> pd.DataFrame:
    """Return the sets released in the first year, sorted by year."""
    ordered = sets.sort_values("year", kind="stable")
    return ordered[ordered["year"] == first_release_year(sets)]


def count_sets_in_year(sets: pd.DataFrame, year: int) -> int:
    """Return how many sets were released in the given year."""
    return int((sets["year"] == year).sum())


def largest_sets(sets: pd.DataFrame, n: int = DEFAULT_LARGEST_SETS) -> pd.DataFrame:
    """Return the n sets with the most parts, largest first."""
    return sets.sort_values("num_parts", ascending=False, kind="stable").head(n)


def sets_by_year(sets: pd.DataFrame) -> pd.DataFrame:
    """Count entries per year; the set_num column holds the number of sets."""
    return sets.groupby("year").count()


def themes_by_year(sets: pd.DataFrame) -> pd.DataFrame:
    """Return the number of distinct themes per year as column nr_themes."""
    per_year = sets.groupby("year").agg({"theme_id": "nunique"})
    return per_year.rename(columns={"theme_id": "nr_themes"})


def parts_per_set(sets: pd.DataFrame) -> pd.DataFrame:
    """Return the average number of parts per set for each year."""
    return sets.groupby("year").agg({"num_parts": "mean"})


def drop_incomplete_years(
    df: pd.DataFrame, n: int = INCOMPLETE_TRAILING_YEARS
) -> pd.DataFrame:
    """Drop the last n rows (years); the 2020 snapshot is incomplete there."""
    return df[:-n] if n > 0 else df


def find_theme_ids(themes: pd.DataFrame, name: str) -> list[int]:
    """Return the ids of all themes with exactly this name."""
    return [int(i) for i in themes.loc[themes["name"] == name, "id"]]


def sets_for_theme_ids(sets: pd.DataFrame, ids: list[int]) -> pd.DataFrame:
    """Return the sets belonging to any of the given theme ids."""
    return sets[sets["theme_id"].isin(ids)]


def set_theme_count(sets: pd.DataFrame) -> pd.DataFrame:
    """Return columns id and set_count, themes with most sets first."""
    counts = sets["theme_id"].value_counts()
    return pd.DataFrame({"id": counts.index, "set_count": counts.to_numpy()})


def merge_theme_names(counts: pd.DataFrame, themes: pd.DataFrame) -> pd.DataFrame:
    """Attach theme names to the counts, keeping the count order."""
    return pd.merge(counts, themes, on="id")


def top_themes(merged: pd.DataFrame, n: int = DEFAULT_TOP_THEMES) -> pd.DataFrame:
    """Return the first n rows of the merged theme counts."""
    return merged.head(n)
