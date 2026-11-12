"""Render one screenshot per lecture step into docs/images/.

Tables and text results are drawn like a notebook cell (code on top, output
below); charts are saved as the figures the library builds. Usage:
    python scripts/make_screenshots.py [output_dir]
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import pandas as pd
from matplotlib.figure import Figure

from lego_analysis.application import analysis
from lego_analysis.infrastructure.data import load_colors, load_sets, load_themes
from lego_analysis.presentation import charts

DEFAULT_OUT = Path(__file__).resolve().parents[1] / "docs" / "images"
CODE_BG = "#f5f5f5"
OUT_BG = "#ffffff"
MONO = "DejaVu Sans Mono"


def cell_image(title: str, code: str, output: str) -> Figure:
    """Draw a notebook-like cell: the step title, the code, then its output."""
    code_lines = code.strip("\n").splitlines()
    out_lines = output.strip("\n").splitlines()
    total = len(code_lines) + len(out_lines) + 4
    fig = Figure(figsize=(11, 0.26 * total + 0.9), facecolor=OUT_BG)
    fig.text(0.02, 0.97, title, fontsize=13, fontweight="bold", va="top")
    code_h = (len(code_lines) + 1) * 0.26 / fig.get_figheight()
    top = 1 - 0.55 / fig.get_figheight()
    fig.patches.append(
        __import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
            (0.01, top - code_h),
            0.98,
            code_h,
            transform=fig.transFigure,
            facecolor=CODE_BG,
            edgecolor="#cccccc",
        )
    )
    fig.text(
        0.02,
        top - 0.1 / fig.get_figheight(),
        "\n".join(code_lines),
        family=MONO,
        fontsize=10,
        va="top",
        color="#1a1a8c",
    )
    fig.text(
        0.02,
        top - code_h - 0.25 / fig.get_figheight(),
        "\n".join(out_lines),
        family=MONO,
        fontsize=10,
        va="top",
    )
    return fig


def frame_text(df: pd.DataFrame) -> str:
    """Return a DataFrame as fixed-width text, like a notebook shows it."""
    return df.to_string()


def build_steps() -> dict[str, Figure]:
    """Build the nine step figures, keyed by file name."""
    colors, sets, themes = load_colors(), load_sets(), load_themes()
    full_sets = analysis.sets_by_year(sets)
    full_themes = analysis.themes_by_year(sets)
    full_parts = analysis.parts_per_set(sets)
    cut = analysis.drop_incomplete_years
    merged = analysis.merge_theme_names(analysis.set_theme_count(sets), themes)
    sw_ids = analysis.find_theme_ids(themes, "Star Wars")
    steps: dict[str, Figure] = {}

    steps["step-1-colours.png"] = cell_image(
        "Step 1: Exploring the brick colours",
        "colors['name'].nunique()\ncolors.groupby('is_trans').count()\n"
        "colors.is_trans.value_counts()",
        f"{analysis.count_unique_colours(colors)}\n\n"
        + frame_text(colors.groupby("is_trans").count())
        + "\n\n"
        + colors.is_trans.value_counts().to_string(),
    )
    steps["step-2-sets.png"] = cell_image(
        "Step 2: The oldest and the largest sets",
        "sets.sort_values('year').head()\nsets[sets['year'] == 1949]\n"
        "sets.sort_values('num_parts', ascending=False).head()",
        "First sets (year "
        f"{analysis.first_release_year(sets)}, "
        f"{analysis.count_sets_in_year(sets, 1949)} sets in 1949):\n"
        + frame_text(analysis.first_sets(sets).head())
        + "\n\nLargest sets:\n"
        + frame_text(analysis.largest_sets(sets)),
    )
    steps["step-3-sets-per-year.png"] = charts.sets_by_year_chart(cut(full_sets))
    steps["step-4-themes-per-year.png"] = charts.themes_by_year_chart(cut(full_themes))
    steps["step-5-two-axes.png"] = charts.sets_and_themes_chart(
        cut(full_sets), cut(full_themes)
    )
    steps["step-6-parts-per-set.png"] = charts.parts_per_set_chart(cut(full_parts))
    steps["step-7-themes-and-keys.png"] = cell_image(
        "Step 7: Themes, primary keys and foreign keys",
        "themes[themes.name == 'Star Wars']\n"
        "sets[sets.theme_id.isin(star_wars_ids)].head()",
        frame_text(themes[themes.name == "Star Wars"])
        + "\n\nSets with these theme ids (first rows):\n"
        + frame_text(analysis.sets_for_theme_ids(sets, sw_ids).head())
        + f"\n\nids found: {sw_ids}",
    )
    steps["step-8-merge.png"] = cell_image(
        "Step 8: Merging DataFrames on a key",
        "set_theme_count = pd.DataFrame({'id': counts.index, 'set_count': counts.values})\n"
        "merged_df = pd.merge(set_theme_count, themes, on='id')\nmerged_df[:5]",
        frame_text(merged.head(5)),
    )
    steps["step-9-bar-chart.png"] = charts.top_themes_bar_chart(
        analysis.top_themes(merged)
    )
    return steps


def main(out_dir: Path) -> None:
    """Write every step image to out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, fig in build_steps().items():
        charts.save_figure(fig, out_dir / name)
        print(f"wrote {out_dir / name}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT)
