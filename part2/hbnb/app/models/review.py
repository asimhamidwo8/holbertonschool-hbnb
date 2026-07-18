from app.models.base_model import BaseModel
from app.models.user import User


class Review(BaseModel):
    """Represents a review in the system."""

    def __init__(self, text, rating, place, user):
        """Initialize a new Review instance."""
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        if not text:
            raise ValueError("text is required")
        if not isinstance(rating, int) or not 1 <= rating <= 5:
            raise ValueError("rating must be an integer between 1 and 5")
        if place is None or not hasattr(place, "add_review"):
            raise ValueError("place must be a valid Place instance")
        if not isinstance(user, User):
            raise ValueError("user must be a valid User instance")

    def __str__(self):
        """Return a string representation of the review."""
        return f"Review({self.rating}/5: {self.text})"
