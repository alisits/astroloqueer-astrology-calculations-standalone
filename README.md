# queerstrology-ephemeris

Standalone Swiss Ephemeris helpers for **house cusps, Ascendant, and Midheaven**. This is the calculation core from Queerstrology, without the frontend, ads scripts, logs, or any API keys.

Planet positions are not implemented yet.

## Requirements

- Python 3.10+
- [pyswisseph](https://pypi.org/project/pyswisseph/) (Swiss Ephemeris bindings)

House calculations do not need extra ephemeris data files.

## Install

```sh
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -e ".[dev]"
```

## Usage

```python
from datetime import datetime
from queerstrology_ephemeris import AstrologyService

service = AstrologyService(52.52, 13.405, datetime(2000, 1, 1, 12, 0, 0))
print(service.get_house_data())
```

Demo (from the repo root):

```sh
# Windows — use the project venv so pyswisseph is available
.venv\Scripts\python.exe demo.py

# after: pip install -e .
python -m queerstrology_ephemeris
```

Running `src\queerstrology_ephemeris\demo.py` with another Python (for example the IDE’s global interpreter) fails with `ModuleNotFoundError` unless that interpreter has this package installed.

## Tests

```sh
pytest
```

## License

This wrapper is released under **GPL-2.0-or-later** so it stays compatible with Swiss Ephemeris / `pyswisseph` (GPL). If you distribute a program that links this library, the GPL terms of Swiss Ephemeris apply. Commercial use of Swiss Ephemeris may require a separate license from [Astrodienst](https://www.astro.com/swisseph/).
