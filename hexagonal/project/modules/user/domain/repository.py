from abc import ABC, abstractmethod
from .models import User


class UserRepository(ABC):
    """Abstract base class for user repository."""
    @abstractmethod
    def create_user(self, user: User) -> None:
        """Create a new user."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        """Retrieve a user by email."""
        pass
