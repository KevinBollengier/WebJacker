import sys
import functions

# TODO refactor to commandline arguments
# TODO refactor static file name


def main():
    try:
        url = input("Enter website to test:")
        test = "reports/filename.md"
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
