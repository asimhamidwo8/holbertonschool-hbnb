import re
from app.models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system."""

    def __init__(self, first_name, last_name, email, is_admin=False):
        """Initializes a new User instance."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        if not first_name or len(first_name) > 50:
            raise ValueError("first_name must be provided and less than 50 characters")
        if not last_name or len(last_name) > 50:
            raise ValueError("last_name must be provided and less than 50 characters")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")

    def __str__(self):
        """Returns a string representation of the user."""
        return f"User({self.first_name} {self.last_name}, {self.email})"
