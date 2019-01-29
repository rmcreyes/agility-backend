"""Represent a data model for a project board."""
from enum import Enum


class BoardPosition(Enum):
    """Represent possible positions on the board for tickets."""

    NEW = 0
    ICEBOX = 1
    BACKLOG = 2
    IN_PROGRESS = 3
    REVIEW = 4
    APPROVED = 5
    DONE = 6
