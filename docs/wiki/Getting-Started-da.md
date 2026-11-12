[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom godt i gang

Krav: Python 3.13 eller nyere. Afhængigheder ved kørsel: `pandas` og `matplotlib`.

Opret og brug et lokalt `.venv` (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kør analysen, testene og notebooken:

```bash
python -m lego_analysis
python -m pytest
jupyter lab notebooks/Lego_Analysis_for_Course.ipynb
```

**Hvad du får ud af det:** en gentagelig opsætning (et virtuelt miljø pr. projekt), en pakke, du installerer i redigerbar tilstand, og tests, der beviser hvert svar.
