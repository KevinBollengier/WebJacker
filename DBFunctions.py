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
        cursor.execute('SELECT * FROM TST')
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
