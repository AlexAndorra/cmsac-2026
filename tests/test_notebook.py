from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).parents[1]


def test_notebook_runs_without_errors():
    notebook = nbformat.read(ROOT / "player_or_team.ipynb", as_version=4)
    NotebookClient(notebook, timeout=1800, kernel_name="python3", resources={"metadata": {"path": str(ROOT)}}).execute()
