import re
from typing import NamedTuple

from db import event_db
from models.user import User
from utils.logconfig import logger


class EventDetails(NamedTuple):
    event_name: str
    event_date: str
    repeat: str


class Event:

    def __init__(self, user_id):
        self.user = User(user_id)
        self.user.save_user()

    def add_event(self, text):
        data = self._parse_text(text)
        event = self.save_and_get_event(*data)
        return EventDetails(
            event_name=event['event_name'],
            event_date=event['event_date'],
            repeat=event['event_remind']
        )

    def _parse_text(self, text):
        pattern = r"^Добавить (.+)\s+(\d{2}.\d{2}.\d{4})\s?(?:повторять каждый (день|месяц|год))?"
        result = re.search(pattern, text)
        logger(result.groups())
        return result.groups()

    def save_and_get_event(self, name, date, repeat):
        user_id = self.user.get_user()['id']
        return event_db.insert_and_get_event(name, date, repeat, user_id)[0]
