[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu. Kebergantungan masa jalan: `pandas` dan `matplotlib`.

Cipta dan gunakan `.venv` tempatan (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jalankan analisis, ujian dan buku nota:

```bash
python -m lego_analysis
python -m pytest
jupyter lab notebooks/Lego_Analysis_for_Course.ipynb
```

**Apa yang anda perolehi:** persediaan yang boleh diulang (satu persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh sunting, dan ujian yang membuktikan setiap jawapan.
