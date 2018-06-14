import requests
import sys
import functions

# TODO refactor to commandline arguments
# TODO refactor static file name
# TODO make program more verbose
# TODO clean up code


def main():
    try:
        # report_output = []

        url = input("Enter website to test:")
        test = "reports/filename.md"
        functions.get_info(test, url)
        functions.verify_https(test, url)
        functions.get_headers(test, url)
        functions.dns_dump(test, url)
        # report_output.append('## DNS Dump ')
        # report_output.append(functions.dns_dump(url, 'CNAME'))
        # report_output.append(functions.dns_dump(url, 'SOA'))
        # report_output.append(functions.dns_dump(url, 'A'))
        # report_output.append(functions.dns_dump(url, 'NS'))
        # report_output.append(functions.dns_dump(url, 'MX'))
        # report_output.append(functions.dns_dump(url, 'HINFO'))
        # report_output.append('## Port Scan')
        # open_ports = functions.simple_portscan(url)
        # for line in open_ports:
        #     report_output.append("\t" + line + "\n")
        # report_output.append('********')
        # functions.print_to_md_file(report_output)
    except KeyboardInterrupt:
        print("[*] User requested an interrupt")
        print("[*] Shutting down")
        sys.exit(1)


if __name__ == '__main__':
    main()
