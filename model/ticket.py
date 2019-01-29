"""Represent the data needed for a development ticket."""
from enum import Enum
import datetime


class Ticket:
    """Represent a ticket with related fields and methods."""

    def __init__(self, ticket_id, creator_id, project_id, title,
                 description, board_pos, ticket_label=None, assignees=None):
        """Create a ticket."""
        self.__ticket_id = ticket_id
        self.__creator_id = creator_id
        self.__project_id = project_id
        self.__title = title
        self.__description = description
        self.__board_pos = board_pos
        self.__ticket_label = ticket_label
        self.__assignees = assignees
        self.__closer_id = None
        self.__closed = False
        self.__creation_date = datetime.datetime.now()


class TicketLabel(Enum):
    """Represent possible labels for tickets."""

    BUG = 0
    FEATURE = 1
    RESEARCH = 2
    DOCS = 3
    TEST = 4
