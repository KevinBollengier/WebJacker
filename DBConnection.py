import pymssql
import json


class DBConnection:

    def __init__(self):
        with open('env.json') as f:
            data = json.load(f)
        self.server = data["server"]
        self.user = data["user"]
        self.password = data["password"]
        self.database = data["database"]
        self.port = data["port"]
        self.db_connection = pymssql.connect(
            server=self.server,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

    def return_connection(self):
        return self.db_connection

