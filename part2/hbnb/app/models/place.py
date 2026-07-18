from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.amenities = []

        if not title or len(title) > 100:
            raise ValueError("title is required and must be <= 100 chars")
        if price < 0:
            raise ValueError("price must be a positive number")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("latitude must be between -90 and 90")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("longitude must be between -180 and 180")

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
