"""Run from the repo root: python demo.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from queerstrology_ephemeris.demo import main

if __name__ == "__main__":
    main()
