""" user domain models """
from dataclasses import dataclass

@dataclass
class User:
    """ user domain model """
    id: int
    username: str
    email: str
    password_hash: str

    # optional for validation
    # def __post_init__(self):
    #     if not self.username:
    #         raise ValueError("Username cannot be empty")
    #     if not self.email:
    #         raise ValueError("Email cannot be empty")