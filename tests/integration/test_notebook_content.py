"""Integration test: the notebook's images and written answers match the data."""

import json
import re
from pathlib import Path
from typing import Any

import pandas as pd

from lego_analysis.application import analysis

NOTEBOOK = (
    Path(__file__).resolve().parents[2] / "notebooks" / "Lego_Analysis_for_Course.ipynb"
)
IMG_SRC = re.compile(r"""<img[^>]*\ssrc=["']([^"']+)["']""", re.IGNORECASE)
GLANCE_HEADING = "## Answers at a glance"
ANSWER_PREFIX = "**Answer"
MIN_ANSWER_CELLS = 5
YEARS = (1949, 1955, 1995, 2019)
PARTS_YEARS = (1954, 2017)


def _cells() -> list[dict[str, Any]]:
    cells: list[dict[str, Any]] = json.loads(NOTEBOOK.read_text(encoding="utf-8"))[
        "cells"
    ]
    return cells


def _source(cell: dict[str, Any]) -> str:
    return "".join(cell["source"])


def _intro() -> str:
    first = _cells()[0]
    assert first["cell_type"] == "markdown"
    return _source(first)


def test_local_images_exist_relative_to_notebook_folder() -> None:
    sources = [
        src
        for cell in _cells()
        if cell["cell_type"] == "markdown"
        for src in IMG_SRC.findall(_source(cell))
        if not src.startswith(("http://", "https://"))
    ]

    assert sources
    missing = [src for src in sources if not (NOTEBOOK.parent / src).is_file()]
    assert missing == []


def test_intro_has_answers_at_a_glance_section() -> None:
    assert GLANCE_HEADING in _intro()


def _glance_text() -> str:
    return _intro().split(GLANCE_HEADING, 1)[1]


def _expected_numbers(sets: pd.DataFrame, themes: pd.DataFrame) -> dict[str, list[str]]:
    biggest = analysis.largest_sets(sets, 1).iloc[0]
    first_year = analysis.first_release_year(sets)
    top = analysis.merge_theme_names(analysis.set_theme_count(sets), themes).iloc[0]
    per_year = analysis.sets_by_year(sets)["set_num"]
    theme_counts = analysis.themes_by_year(sets)["nr_themes"]
    parts = analysis.parts_per_set(sets)["num_parts"]
    return {
        "largest set": [f"{int(biggest['num_parts']):,}", str(biggest["name"])],
        "first year": [
            str(first_year),
            str(analysis.count_sets_in_year(sets, first_year)),
        ],
        "top theme": [str(top["name"]), str(int(top["set_count"]))],
        "sets per year": [f"{int(per_year.loc[y])} ({y})" for y in YEARS],
        "themes per year": [f"{int(theme_counts.loc[y])} ({y})" for y in YEARS],
        "average parts": [str(round(float(parts.loc[y]))) for y in PARTS_YEARS],
    }


def test_intro_answers_match_computed_values(
    sets: pd.DataFrame, themes: pd.DataFrame
) -> None:
    text = _glance_text()

    for topic, values in _expected_numbers(sets, themes).items():
        for value in values:
            assert value in text, f"{topic}: {value!r} not in the intro"


def test_each_question_has_an_answer_cell_after_a_code_cell() -> None:
    cells = _cells()
    answers = [
        i for i, cell in enumerate(cells) if _source(cell).startswith(ANSWER_PREFIX)
    ]

    assert len(answers) >= MIN_ANSWER_CELLS
    for i in answers:
        assert i > 0
        assert cells[i]["cell_type"] == "markdown"
        assert cells[i - 1]["cell_type"] == "code", f"cell {i} does not follow code"
