import pymssql


class DBConnection:
    def __init__(self):
        self.db_connection = pymssql.connect(
            server='DESKTOP-M2QTFTB\SQLEXPRESS',
            user='TST',
            password='TST',
            database='TST',
            port=60072
        )

    def return_connection(self):
        return self.db_connection

