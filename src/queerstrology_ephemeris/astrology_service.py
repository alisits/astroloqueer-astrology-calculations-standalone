from .house_calculator import AstrologicalHouses


class AstrologyService:
    def __init__(self, latitude, longitude, utc_datetime):
        self.latitude = latitude
        self.longitude = longitude
        self.utc_datetime = utc_datetime

    def get_house_data(self):
        house_calculator = AstrologicalHouses(
            self.latitude, self.longitude, self.utc_datetime
        )
        return house_calculator.get_house_cusps()
