import requests
import socket
import sys
import functions

# TODO refactor to commandline arguments
# TODO refactor static file name
# TODO make program more verbose
# TODO clean up code
try:
    report_output = []

    url = input("Enter website to test:")

    r = requests.get(url="http://" + url)
    report_output.append('# W3bJ4ck3r Report - ' + url)
    report_output.append('## General Information')
    report_output.append('\tURL : ' + url)
    report_output.append('\tStatus Code : ' + str(r.status_code))
    try:
        sr = requests.get(url="https://" + url, verify=True)
        report_output.append("\tHTTPS : OK")
        if 'strict-transport-security' in sr.headers:
            report_output.append('\tHSTS : Yes')
        else:
            report_output.append("\tHSTS : No")
    except requests.exceptions.SSLError:
        report_output.append("\tHTTPS : Errors with HTTPS certificate.")
    report_output.append('## Request Headers')
    for header in r.request.headers:
        report_output.append("\t" + header + " : " + r.request.headers[header])
    report_output.append('## Response Headers')
    for header in r.headers:
        report_output.append("\t" + header + " : " + r.headers[header])
    report_output.append('## DNS Dump ')
    report_output.append(functions.dns_dump(url, 'CNAME'))
    report_output.append(functions.dns_dump(url, 'SOA'))
    report_output.append(functions.dns_dump(url, 'A'))
    report_output.append(functions.dns_dump(url, 'NS'))
    report_output.append(functions.dns_dump(url, 'MX'))
    report_output.append(functions.dns_dump(url, 'HINFO'))
    report_output.append('## Port Scan')
    open_ports = functions.simple_portscan(url, 1025)
    for line in open_ports:
        report_output.append("\t"+line+"\n")
    report_output.append('********')
    functions.print_to_md_file(report_output)
except KeyboardInterrupt:
    print("[*] User requested an interrupt")
    print("[*] Shutting down")
    sys.exit(1)
