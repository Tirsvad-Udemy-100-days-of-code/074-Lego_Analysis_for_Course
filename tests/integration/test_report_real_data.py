import pytest

from lego_analysis.application.report import build_report
from lego_analysis.infrastructure.data import load_colors, load_sets, load_themes
from lego_analysis.presentation.cli import main


@pytest.fixture(scope="module")
def report() -> str:
    return build_report(load_colors(), load_sets(), load_themes())


def test_report_names_the_largest_set(report: str) -> None:
    assert "The Ultimate Battle for Chima" in report
    assert "9987" in report


def test_report_gives_first_year_and_its_sets(report: str) -> None:
    assert "First release year: 1949 with 5 sets" in report


def test_report_names_top_theme(report: str) -> None:
    assert "Star Wars (753 sets)" in report


def test_report_compares_1955_and_2019(report: str) -> None:
    assert "In 1955: 28 sets and 4 themes" in report
    assert "In 2019: 840 sets and 78 themes" in report


def test_report_compares_average_parts(report: str) -> None:
    assert "in 1954: 12.4" in report
    assert "in 2017: 221.8" in report


def test_report_states_colour_figures(report: str) -> None:
    assert "Unique colours: 135 (107 opaque, 28 transparent)" in report


def test_cli_prints_the_report(report: str, capsys: pytest.CaptureFixture[str]) -> None:
    main()

    assert capsys.readouterr().out == report
