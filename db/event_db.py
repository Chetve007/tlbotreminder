from db.db_config import DbConfig

DB = DbConfig()

SQL_INSERT_EVENT = '''
INSERT INTO "event"(event_name, event_date, event_remind, user_id) VALUES(%s, to_date(%s, 'DD.MM.YYYY'), %s, %s)
RETURNING *
'''


def insert_and_get_event(name: str, date: str, repeat: str, user_id: int):
    repeat = 'Yes' if repeat else 'No'
    return DB.execute(SQL_INSERT_EVENT, (name, date, repeat, user_id), action='fetch_commit')
