"""Presentation: build matplotlib figures from prepared DataFrames."""

from pathlib import Path

import pandas as pd
from matplotlib.figure import Figure

SETS_COLOUR = "tab:blue"
THEMES_COLOUR = "tab:green"


def save_figure(fig: Figure, path: Path | str) -> None:
    """Write the figure to an image file."""
    fig.savefig(Path(path))


def sets_by_year_chart(sets_per_year: pd.DataFrame) -> Figure:
    """Line chart of the number of sets released per year."""
    fig = Figure()
    ax = fig.add_subplot()
    ax.plot(sets_per_year.index, sets_per_year["set_num"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Sets")
    return fig


def themes_by_year_chart(themes_per_year: pd.DataFrame) -> Figure:
    """Line chart of the number of themes per year."""
    fig = Figure()
    ax = fig.add_subplot()
    ax.plot(themes_per_year.index, themes_per_year["nr_themes"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Themes")
    return fig


def sets_and_themes_chart(
    sets_per_year: pd.DataFrame, themes_per_year: pd.DataFrame
) -> Figure:
    """Sets and themes per year on two y axes."""
    fig = Figure()
    ax_sets = fig.add_subplot()
    ax_themes = ax_sets.twinx()
    ax_sets.plot(sets_per_year.index, sets_per_year["set_num"], color=SETS_COLOUR)
    ax_themes.plot(
        themes_per_year.index, themes_per_year["nr_themes"], color=THEMES_COLOUR
    )
    ax_sets.set_xlabel("Year")
    ax_sets.set_ylabel("Number of Sets", color=SETS_COLOUR)
    ax_sets.tick_params(axis="y", labelcolor=SETS_COLOUR)
    ax_themes.set_ylabel("Number of Themes", color=THEMES_COLOUR)
    ax_themes.tick_params(axis="y", labelcolor=THEMES_COLOUR)
    return fig


def parts_per_set_chart(parts_per_year: pd.DataFrame) -> Figure:
    """Scatter plot of the average parts per set by year."""
    fig = Figure()
    ax = fig.add_subplot()
    ax.scatter(parts_per_year.index, parts_per_year["num_parts"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Parts per Set")
    return fig


def top_themes_bar_chart(merged: pd.DataFrame) -> Figure:
    """Bar chart of theme names against their number of sets."""
    fig = Figure(figsize=(14, 8))
    ax = fig.add_subplot()
    ax.bar(merged["name"], merged["set_count"])
    ax.set_xlabel("Theme Name", fontsize=14)
    ax.set_ylabel("Nr of Sets", fontsize=14)
    ax.tick_params(axis="x", labelrotation=45, labelsize=14)
    ax.tick_params(axis="y", labelsize=14)
    return fig
