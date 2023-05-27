from db.db_config import DbConfig

DB = DbConfig()


def insert_user(user_id: int):
    DB.execute('INSERT INTO "user" (tl_user_id) VALUES (%s)', (user_id,), action='commit')


def select_user_by_tl_id(tl_user_id: int):
    return DB.execute('SELECT * FROM "user" WHERE tl_user_id = %s', (tl_user_id,))
