from DBConnection import DBConnection
from typing import *


class DBFunctions:
    db_instance = DBConnection()
    db_connection = db_instance.return_connection()

    def get_ports(self)->List[Tuple[int, str]]:
        """
        Function that retrieves port list with services from DB
        :return: List of tuples in format (port, service)
        """
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT * FROM PortsServices')
        port_services = []
        row = cursor.fetchone()
        while row:
            port_services.append(row)
            row = cursor.fetchone()
        return port_services

    def get_websites(self)->List[str]:
        cursor = self.db_connection.cursor()
        cursor.execute('Select URL from Websites')
        web_urls = []
        row = cursor.fetchone()
        while row:
            web_urls.append(row[0])
            row = cursor.fetchone()
        return web_urls

    def trunc_error_table(self):
        conn = self.db_connection
        cursor = conn.cursor()
        cursor.execute('Truncate table HttpsErrors')
        conn.commit()

    def insert_https_error(self, url):
        conn = self.db_connection
        cursor = conn.cursor()
        cursor.execute("insert into HttpsErrors VALUES (%s)", url)
        conn.commit()

