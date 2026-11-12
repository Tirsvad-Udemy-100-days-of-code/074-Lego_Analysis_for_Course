from pathlib import Path

import pandas as pd
from matplotlib.figure import Figure

from lego_analysis.application.analysis import (
    drop_incomplete_years,
    merge_theme_names,
    parts_per_set,
    set_theme_count,
    sets_by_year,
    themes_by_year,
    top_themes,
)
from lego_analysis.presentation.charts import (
    parts_per_set_chart,
    save_figure,
    sets_and_themes_chart,
    sets_by_year_chart,
    themes_by_year_chart,
    top_themes_bar_chart,
)


def test_sets_by_year_chart_has_one_axis_and_one_line(sets: pd.DataFrame) -> None:
    fig = sets_by_year_chart(drop_incomplete_years(sets_by_year(sets)))

    assert isinstance(fig, Figure)
    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 1


def test_sets_by_year_chart_excludes_incomplete_years(sets: pd.DataFrame) -> None:
    per_year = drop_incomplete_years(sets_by_year(sets))

    fig = sets_by_year_chart(per_year)

    assert len(fig.axes[0].lines[0].get_xdata()) == len(per_year)


def test_themes_by_year_chart_has_one_line(sets: pd.DataFrame) -> None:
    fig = themes_by_year_chart(drop_incomplete_years(themes_by_year(sets)))

    assert len(fig.axes) == 1
    assert len(fig.axes[0].lines) == 1


def test_sets_and_themes_chart_has_two_axes(sets: pd.DataFrame) -> None:
    fig = sets_and_themes_chart(
        drop_incomplete_years(sets_by_year(sets)),
        drop_incomplete_years(themes_by_year(sets)),
    )

    assert len(fig.axes) == 2
    assert all(len(ax.lines) == 1 for ax in fig.axes)


def test_sets_and_themes_chart_colours_the_axis_labels(sets: pd.DataFrame) -> None:
    fig = sets_and_themes_chart(sets_by_year(sets), themes_by_year(sets))

    colours = {ax.yaxis.label.get_color() for ax in fig.axes}
    assert len(colours) == 2


def test_parts_per_set_chart_is_a_scatter(sets: pd.DataFrame) -> None:
    fig = parts_per_set_chart(drop_incomplete_years(parts_per_set(sets)))

    ax = fig.axes[0]
    assert len(ax.collections) == 1
    assert len(ax.lines) == 0


def test_top_themes_bar_chart_layout(sets: pd.DataFrame, themes: pd.DataFrame) -> None:
    merged = top_themes(merge_theme_names(set_theme_count(sets), themes))

    fig = top_themes_bar_chart(merged)

    ax = fig.axes[0]
    assert tuple(fig.get_size_inches()) == (14, 8)
    assert len(ax.patches) == 10
    assert ax.get_ylabel() == "Nr of Sets"
    assert ax.get_xlabel() == "Theme Name"
    assert ax.get_xticklabels()[0].get_rotation() == 45


def test_save_figure_writes_png(sets: pd.DataFrame, tmp_path: Path) -> None:
    target = tmp_path / "chart.png"

    save_figure(sets_by_year_chart(sets_by_year(sets)), target)

    assert target.stat().st_size > 0


def test_chart_on_empty_frame_has_no_data_points() -> None:
    empty = pd.DataFrame({"set_num": []}, index=pd.Index([], name="year"))

    fig = sets_by_year_chart(empty)

    assert len(fig.axes[0].lines[0].get_xdata()) == 0
