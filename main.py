import requests
import socket
import sys
import functions

try:
    print("Enter website to test:")
    url = input()

    r = requests.get(url="http://" + url)
    print('****************** General Information ******************')
    print('\tURL : ' + url)
    print('\tStatus Code : ' + str(r.status_code))
    try:
        sr = requests.get(url="https://" + url, verify=True)
        print("\tHTTPS : OK")
        if 'strict-transport-security' in sr.headers:
            print('\tHSTS : Yes')
        else:
            print("\tHSTS : No")
    except requests.exceptions.SSLError:
        print("\tHTTPS : Errors with HTTPS certificate.")
    print('****************** Request Headers ******************')
    for header in r.request.headers:
        print("\t" + header + " : " + r.request.headers[header])
    print('****************** Response Headers ******************')
    for header in r.headers:
        print("\t" + header + " : " + r.headers[header])
    print('****************** DNS Dump ******************')
    functions.dns_dump(url, 'CNAME')
    functions.dns_dump(url, 'A')
    functions.dns_dump(url, 'NS')
    functions.dns_dump(url, 'MX')
    functions.dns_dump(url, 'HINFO')
    print('****************** Port Scan ******************')
    remote_server_ip = socket.gethostbyname(url)
    functions.simple_portscan(remote_server_ip, 1025)
    print('***********************************************')
except KeyboardInterrupt:
    print("[*] User requested an interrupt")
    print("[*] Shutting down")
    sys.exit(1)
