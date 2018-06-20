import sys
import functions
from DBFunctions import DBFunctions
from datetime import datetime
import os
import shutil


# TODO add length of scan


def main():
    database = DBFunctions()
    websites = database.get_websites()
    # websites = ["www.brightfish.be", "www.kinepolis.be"]
    database.trunc_error_tables()

    folder = "reports/{date}".format(date=datetime.today().strftime('%d-%m-%y'))
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        shutil.rmtree(folder)
        os.makedirs(folder)

    for url in websites:
        try:
            print("Webjacking : {url}".format(url=url))
            file_path = "reports/{date}/{url}.md".format(date=datetime.today().strftime('%d-%m-%y'), url=url)
            functions.get_info(file_path, url)
            functions.verify_https(file_path, url)
            functions.get_headers(file_path, url)
            functions.check_clickjacking(file_path, url)
            functions.dns_dump(file_path, url)
            functions.simple_port_scan(file_path, url)
        except KeyboardInterrupt:
            print("[*] User requested an interrupt")
            print("[*] Shutting down")
            sys.exit(1)


if __name__ == '__main__':
    main()
