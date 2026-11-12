from pathlib import Path

import pandas as pd

from lego_analysis.infrastructure.data import (
    DATA_DIR,
    load_colors,
    load_sets,
    load_themes,
)


def test_data_dir_points_to_project_data_folder() -> None:
    assert (DATA_DIR / "sets.csv").is_file()


def test_load_colors_has_expected_columns() -> None:
    assert list(load_colors().columns) == ["id", "name", "rgb", "is_trans"]


def test_load_sets_has_expected_columns() -> None:
    expected = ["set_num", "name", "year", "theme_id", "num_parts"]
    assert list(load_sets().columns) == expected


def test_load_themes_has_expected_columns() -> None:
    assert list(load_themes().columns) == ["id", "name", "parent_id"]


def test_load_colors_reads_from_custom_directory(tmp_path: Path) -> None:
    (tmp_path / "colors.csv").write_text("id,name,rgb,is_trans\n1,Red,FF0000,f\n")

    result = load_colors(tmp_path)

    assert isinstance(result, pd.DataFrame)
    assert result["name"].tolist() == ["Red"]


def test_load_sets_accepts_string_directory(tmp_path: Path) -> None:
    (tmp_path / "sets.csv").write_text(
        "set_num,name,year,theme_id,num_parts\nx-1,X,1999,1,3\n"
    )

    assert load_sets(str(tmp_path))["num_parts"].tolist() == [3]
