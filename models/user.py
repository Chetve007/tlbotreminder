from db import user_db
from utils.logconfig import logger


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def save_user(self):
        if self._is_exist():
            logger(f'User - {self.user_id} exists')
        else:
            user_db.insert_user(self.user_id)
            logger(f'Create user - {self.user_id}')

    def _is_exist(self) -> bool:
        user = self.get_user()
        return True if user else False

    def get_user(self):
        user = user_db.select_user_by_tl_id(self.user_id)
        return user[0] if user else None
