import sys
import functions
from DBFunctions import DBFunctions

# TODO refactor file name reporting with date time


def main():
    database = DBFunctions()
    websites = database.get_websites()
    for url in websites:
        try:
            # url = input("Enter website to test:")
            test = "reports/{url}.md".format(url=url)
            functions.get_info(test, url)
            functions.verify_https(test, url)
            functions.get_headers(test, url)
            functions.dns_dump(test, url)
            functions.simple_port_scan(test, url)
        except KeyboardInterrupt:
            print("[*] User requested an interrupt")
            print("[*] Shutting down")
            sys.exit(1)


if __name__ == '__main__':
    main()
