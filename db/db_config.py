from configparser import ConfigParser

import psycopg2
from psycopg2 import DatabaseError
from psycopg2.extras import DictCursor

from utils.logconfig import logger


class DbConfig:

    def __init__(self, filename='database.ini', section='postgresql', schema='public'):
        self.filename = filename
        self.section = section
        self.schema = schema
        self.parser = ConfigParser()
        self.connect = None

    def connection(self):
        self.parser.read(self.filename)
        if self.parser.has_section(self.section):
            params = self.parser.items(self.section)
            db = {k: v for k, v in params}
            db.update(options=f'-c search_path={self.schema}' if self.schema else {})

            logger('Going to connect to the DB')
            self.connect = psycopg2.connect(**db)
        else:
            raise Exception('Section {0} not found in the {1} file'.format(self.section, self.filename))

    def disconnection(self):
        logger('Going to disconnect from the DB')
        if self.connect:
            self.connect.close()
            logger('Disconnected!')

    def execute(self, raw_sql: str, sql_params: tuple, action='fetch'):
        result = None
        logger(f'Execute request: {raw_sql % sql_params}')
        self.connection()

        try:
            with self.connect.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(raw_sql, sql_params)

                match action:
                    case 'fetch':
                        result = cursor.fetchall()
                    case 'commit':
                        self.connect.commit()
                    case 'fetch_commit':
                        result = cursor.fetchall()
                        self.connect.commit()

        except DatabaseError as e:
            logger(e.pgerror)
        finally:
            self.disconnection()

        logger('Execution in DB was successful!')
        return result
