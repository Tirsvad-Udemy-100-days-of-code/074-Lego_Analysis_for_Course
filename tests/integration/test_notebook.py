"""Integration test: the course notebook runs from top to bottom."""

from pathlib import Path

import pytest

NOTEBOOK = (
    Path(__file__).resolve().parents[2] / "notebooks" / "Lego_Analysis_for_Course.ipynb"
)
MIN_CODE_CELLS = 20
TIMEOUT_SECONDS = 120


def test_notebook_executes_without_error() -> None:
    """Run an in-memory copy of the notebook; the repo file is not changed."""
    nbformat = pytest.importorskip("nbformat", reason="nbformat is not installed")
    nbclient = pytest.importorskip("nbclient", reason="nbclient is not installed")
    pytest.importorskip("ipykernel", reason="ipykernel is not installed")

    notebook = nbformat.read(NOTEBOOK, as_version=4)
    client = nbclient.NotebookClient(
        notebook,
        timeout=TIMEOUT_SECONDS,
        kernel_name="python3",
        resources={"metadata": {"path": str(NOTEBOOK.parent)}},
    )
    client.execute()

    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    assert len(code_cells) >= MIN_CODE_CELLS
