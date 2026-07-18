from app.models.base_model import BaseModel
from app.models.user import User

class Place(BaseModel):
    """Represents a place in the system."""

    def __init__(self, title, description, price, latitude, longitude, owner):
        """Initializes a new Place instance."""
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []
        if not title or len(title) > 100:
            raise ValueError("title is required and must be less than 100 characters")
        if price is None or float(price) <= 0:
            raise ValueError("price must be a positive number")
        if latitude is None or not -90.0 <= float(latitude) <= 90.0:
            raise ValueError("latitude must be between -90 and 90")
        if longitude is None or not -180.0 <= float(longitude) <= 180.0:
            raise ValueError("longitude must be between -180 and 180")
        if owner is None or not isinstance(owner, User):
            raise ValueError("owner must be a User instance")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def __str__(self):
        """Return a string representation of the place."""
        return f"Place({self.title}, {self.price})"
