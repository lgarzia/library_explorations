import sqlite3

from injector import Injector, Module, inject, provider, singleton


class RequestHandler:
    @inject
    def __init__(self, db: sqlite3.Connection):
        self._db = db

    def get(self):
        cursor = self._db.cursor()
        cursor.execute("SELECT key, value FROM data ORDER by key")
        return cursor.fetchall()


class Configuration:
    def __init__(self, connection_string):
        self.connection_string = connection_string


def configure_for_testing(binder):
    configuration = Configuration(":memory:")
    binder.bind(Configuration, to=configuration, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provide_sqlite_connection(
        self, configuration: Configuration
    ) -> sqlite3.Connection:
        conn = sqlite3.connect(configuration.connection_string)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data (key PRIMARY KEY, value)")
        cursor.execute('INSERT OR REPLACE INTO data VALUES ("hello", "world")')
        return conn


injector = Injector([configure_for_testing, DatabaseModule()])
handler = injector.get(RequestHandler)
tuple(map(str, handler.get()[0]))  # py3/py2 compatibility hack
("hello", "world")
