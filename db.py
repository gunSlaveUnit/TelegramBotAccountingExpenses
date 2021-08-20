import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from envparser import EnvParser

config = EnvParser.parse()


class DBClient:
    def __init__(self, database, user, password, host, port):
        self._database = database
        self._user = user
        self._password = password
        self._host = host
        self._port = port

        # We connect to the default database (postgres), then check the database for existence
        self._connection, self._cursor = self._create_new_conn_cur()
        self._connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        if not self._check_db_exists():
            self._create_basic_db_structure()

    def _create_new_conn_cur(self, dbname='postgres'):
        connection = psycopg2.connect(dbname=dbname,
                                      user=self._user,
                                      password=self._password,
                                      host=self._host,
                                      port=self._port)
        cursor = connection.cursor()
        return connection, cursor

    def _check_db_exists(self):
        query_check_db_exists = f"SELECT 1 FROM pg_database WHERE datname='{self._database}'"
        self._cursor.execute(query_check_db_exists)
        return self._cursor.fetchone()

    def _create_basic_db_structure(self):
        query_create_new_empty_db = f'CREATE DATABASE {self._database};'
        self._cursor.execute(query_create_new_empty_db)
        self._cursor.close()
        self._connection.close()

        # We are connecting to the new empty created database
        self._create_new_conn_cur(dbname=self._database)

        with open(config['DB_BASE_CONFIG_FILENAME'], 'r') as sql_file:
            query_create_base_struct = sql_file.read()
            self._cursor.execute(query_create_base_struct)


if __name__ == '__main__':
    client = DBClient(database=config['DB_NAME'],
                      user=config['DB_USER'], password=config['DB_PASS'],
                      host=config['DB_HOST'], port=config['DB_PORT'])
