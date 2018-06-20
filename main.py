import sys
import functions
from DBFunctions import DBFunctions
import datetime

# TODO refactor file name reporting with date time
# TODO add length of scan


def main():
    database = DBFunctions()
    websites = database.get_websites()
    database.trunc_error_tables()
    for url in websites:
        try:
            print("Webjacking : {url}".format(url=url))
            test = "reports/{date}/{url}.md".format(date=datetime.datetime.today().strftime('%d-%m-%y'), url=url)
            functions.get_info(test, url)
            functions.verify_https(test, url)
            functions.get_headers(test, url)
            functions.check_clickjacking(test, url)
            functions.dns_dump(test, url)
            functions.simple_port_scan(test, url)
        except KeyboardInterrupt:
            print("[*] User requested an interrupt")
            print("[*] Shutting down")
            sys.exit(1)


if __name__ == '__main__':
    main()
