from datetime import datetime

from queerstrology_ephemeris import AstrologyService, AstrologicalHouses


BERLIN = (52.52, 13.405)
J2000 = datetime(2000, 1, 1, 12, 0, 0)


def test_julian_day_is_j2000():
    houses = AstrologicalHouses(*BERLIN, J2000)
    assert houses.julian_day == 2451545.0


def test_house_cusps_have_twelve_values_in_longitude_range():
    result = AstrologyService(*BERLIN, J2000).get_house_data()
    cusps = result["house_cusps"]

    assert len(cusps) == 12
    assert all(0 <= cusp < 360 for cusp in cusps)
    assert 0 <= result["ascendant"] < 360
    assert 0 <= result["midheaven"] < 360


def test_berlin_j2000_angles_match_swiss_ephemeris():
    result = AstrologyService(*BERLIN, J2000).get_house_data()

    # Placidus, Swiss Ephemeris, Berlin 52.52N 13.405E, 2000-01-01 12:00 UTC
    assert result["ascendant"] == 51.63
    assert result["midheaven"] == 292.09
    assert result["house_cusps"][0] == result["ascendant"]
    assert result["house_cusps"][9] == result["midheaven"]
