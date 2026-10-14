import swisseph as swe


class AstrologicalHouses:
    def __init__(self, latitude, longitude, utc_datetime, house_system="P"):
        self.latitude = latitude
        self.longitude = longitude
        self.utc_datetime = utc_datetime
        if isinstance(house_system, str):
            house_system = house_system.encode("ascii")
        self.house_system = house_system
        self.julian_day = self.calculate_julian_day()

    def calculate_julian_day(self):
        ut_hours = (
            self.utc_datetime.hour
            + self.utc_datetime.minute / 60
            + self.utc_datetime.second / 3600
        )
        return swe.julday(
            self.utc_datetime.year,
            self.utc_datetime.month,
            self.utc_datetime.day,
            ut_hours,
            swe.GREG_CAL,
        )

    def calculate_houses(self):
        cusps, angles = swe.houses(
            self.julian_day, self.latitude, self.longitude, self.house_system
        )
        return cusps, angles

    def get_house_cusps(self):
        cusps, angles = self.calculate_houses()
        return {
            "house_cusps": [round(cusp, 2) for cusp in cusps],
            "ascendant": round(angles[0], 2),
            "midheaven": round(angles[1], 2),
        }
