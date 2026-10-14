from datetime import datetime
import sys
from pathlib import Path

# Allow `python src/queerstrology_ephemeris/demo.py` without an editable install.
_src_root = Path(__file__).resolve().parents[1]
if str(_src_root) not in sys.path:
    sys.path.insert(0, str(_src_root))

from queerstrology_ephemeris import AstrologyService

def main():
    # Example: Berlin, 1 January 2000, 12:00 UTC (J2000.0)
    latitude = 52.52
    longitude = 13.405
    utc_datetime = datetime(2000, 1, 1, 12, 0, 0)

    astrology_service = AstrologyService(latitude, longitude, utc_datetime)
    houses = astrology_service.get_house_data()

    print("House Cusps:", houses["house_cusps"])
    print("Ascendant:", houses["ascendant"])
    print("Midheaven:", houses["midheaven"])


if __name__ == "__main__":
    main()
