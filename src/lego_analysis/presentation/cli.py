"""Command line: load the data, build the report and print it."""

from lego_analysis.application.report import build_report
from lego_analysis.infrastructure.data import load_colors, load_sets, load_themes


def main() -> None:
    """Print the report for the bundled data set."""
    print(build_report(load_colors(), load_sets(), load_themes()), end="")
