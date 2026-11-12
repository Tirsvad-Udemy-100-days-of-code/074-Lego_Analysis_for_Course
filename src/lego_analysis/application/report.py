"""Answer the assignment questions as plain text."""

import pandas as pd

from lego_analysis.application import analysis
from lego_analysis.domain.rules import (
    AVERAGE_PARTS_YEARS,
    OPAQUE_FLAG,
    SETS_AND_THEMES_YEARS,
    TRANSPARENT_FLAG,
)


def _value(df: pd.DataFrame, year: int, column: str) -> float:
    return float(df[column].astype(float).to_numpy()[df.index.get_loc(year)])


def build_report(colors: pd.DataFrame, sets: pd.DataFrame, themes: pd.DataFrame) -> str:
    """Return a plain-text report with the key figures of the dataset."""
    biggest = analysis.largest_sets(sets, 1).iloc[0]
    first_year = analysis.first_release_year(sets)
    merged = analysis.merge_theme_names(analysis.set_theme_count(sets), themes)
    top = merged.iloc[0]
    per_year = analysis.sets_by_year(sets)
    theme_counts = analysis.themes_by_year(sets)
    parts = analysis.parts_per_set(sets)
    flags = analysis.transparent_counts_groupby(colors)

    lines = [
        "LEGO analysis",
        f"Unique colours: {analysis.count_unique_colours(colors)} "
        f"({flags.get(OPAQUE_FLAG, 0)} opaque, "
        f"{flags.get(TRANSPARENT_FLAG, 0)} transparent)",
        f"Largest set: {biggest['name']} ({biggest['set_num']}) "
        f"with {int(biggest['num_parts'])} parts",
        f"First release year: {first_year} with "
        f"{analysis.count_sets_in_year(sets, first_year)} sets",
        f"Theme with most sets: {top['name']} ({int(top['set_count'])} sets)",
    ]
    for year in SETS_AND_THEMES_YEARS:
        lines.append(
            f"In {year}: {int(_value(per_year, year, 'set_num'))} sets "
            f"and {int(_value(theme_counts, year, 'nr_themes'))} themes"
        )
    for year in AVERAGE_PARTS_YEARS:
        lines.append(
            f"Average parts per set in {year}: {_value(parts, year, 'num_parts'):.1f}"
        )
    return "\n".join(lines) + "\n"
