import pandas as pd

from lego_analysis.application.report import build_report


def test_report_uses_the_given_frames() -> None:
    colors = pd.DataFrame(
        {"id": [1], "name": ["Red"], "rgb": ["FF0000"], "is_trans": ["f"]}
    )
    years = (1949, 1954, 1955, 2017, 2019)
    sets = pd.DataFrame(
        {
            "set_num": [f"s{y}-1" for y in years],
            "name": [f"Set{y}" for y in years],
            "year": list(years),
            "theme_id": [1] * len(years),
            "num_parts": [y % 100 for y in years],
        }
    )
    themes = pd.DataFrame({"id": [1], "name": ["Only"], "parent_id": [None]})

    text = build_report(colors, sets, themes)

    assert "Unique colours: 1 (1 opaque, 0 transparent)" in text
    assert "Only (5 sets)" in text
