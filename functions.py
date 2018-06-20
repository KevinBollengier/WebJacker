import dns.resolver
import requests
from socket import *
from DBFunctions import DBFunctions


def get_info(file, url: str):
    print('Getting general info...')
    output = open(file, 'a')
    try:
        r = requests.get(url="http://" + url)
        output.write('# W3bJ4ck3r Report - ' + url + '\n')
        output.write('## General information'+'\n')
        output.write('\tURL : ' + url + '\n')
        output.write('\tStatus Code: ' + str(r.status_code) + '\n')
    except requests.exceptions.ConnectionError:
        output.write('\tStatus Code : No connection could be made because the target machine actively refused it.')
    output.close()

# TODO: verify if clickjacking is possible


def check_clickjacking(file, url: str):
    print('Checking for clickjacking ...')
    output = open(file, 'a')
    db_functions = DBFunctions()
    try:
        r = requests.get(url="https://" + url, verify=True)
        print(r.headers)
        if 'X-Frame-Options' in r.headers.keys() or 'Content-Security-Policy' in r.headers.keys():
            output.write('\tVulnerable to clickjacking : NO\n')
        else:
            output.write('\tVulnerable to clickjacking : Yes\n')

    except requests.exceptions.SSLError:
        print('SSL Exception during clicjack verification...')
        db_functions.insert_clickjack_website(url)


def verify_https(file, url: str):
    print('Verifying https...')
    db_func = DBFunctions()
    output = open(file, 'a')
    try:
        r = requests.get(url="https://" + url, verify=True)
        output.write('\tHTTPS : OK' + '\n')
        if 'strict-transport-security' in r.headers:
            output.write('\tHSTS : Yes' + '\n')
        else:
            output.write('\tHSTS : No' + '\n')
    except requests.exceptions.SSLError:
        output.write('\tHTTPS : Errors with HTTPS certificate.\n')
        db_func.insert_https_error(url)
    except requests.exceptions.ConnectionError:
        print("No connection, machine refused it.")
    output.close()


def get_headers(file, url: str):
    print('Grabbing http headers...')
    output = open(file, 'a')
    try:
        r = requests.get('https://' + url, verify=True)
        output.write('## Request Headers\n')
        for header in r.request.headers:
            output.write('\t' + header + ' : ' + r.request.headers[header] + '\n')
        output.write('## Response Headers\n')
        for header in r.headers:
            output.write('\t' + header + ' : ' + r.headers[header] + '\n')
        output.close()
    except requests.exceptions.SSLError:
        output.close()
    except requests.exceptions.ConnectionError:
        output.close()


def get_dns_info(url, record):
    """
    Function that queries DNS records based on url and the type of record provided in the parameters
    :param url: the url that needs to be queried
    :param record: Type of DNS record to query
    """
    dns_records = []
    try:
        answer = dns.resolver.query(url, record)
        print('Found ' + str(len(answer)) + ' ' + str(record) + ' record(s).')

        for data in answer:
            dns_records.append("\t{dns_record} : ".format(dns_record=record) + str(data))
        return dns_records
    except dns.resolver.NoAnswer:
        dns_records.append("\t{dns_record} : No information.".format(dns_record=record))
        return dns_records
    except dns.resolver.NoNameservers:
        dns_records.append("\tShit happened.")
        return dns_records


def dns_dump(file, url):
    record_names = ['CNAME', 'SOA', 'A', 'NS', 'MX', 'HINFO']
    output = open(file, 'a')
    print('Grabbing DNS records')
    output.write('## DNS Dump\n')
    dns_records = []
    for record_name in record_names:
            dns_records.append(get_dns_info(url, record_name))
    for dns_record in dns_records:
        for subrecord in dns_record:
            output.write(subrecord+'\n')
    output.close()


def simple_port_scan(file, url):
    """
    Simple portscan to see if a port is open
    :param file: filename
    :param url: host to be scanned
    """
    output = open(file, 'a')
    remote_host_ip = gethostbyname(url)
    db_functions = DBFunctions()
    ports_services = db_functions.get_ports()
    output.write('## Port Scan\n')
    print("Scanning: " + str(remote_host_ip))
    # open_ports = []
    amount_open_ports = 0
    for (port, service) in ports_services:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.05)
        result = s.connect_ex((remote_host_ip, port))
        if result == 0:
            output.write("\tPort {port}: \t open    {service}".format(port=port, service=service) + '\n')
            amount_open_ports = amount_open_ports + 1
        s.close()
    print(url + ' has {nrPorts} open port(s).'.format(nrPorts=str(amount_open_ports)))
    output.write("****")
    output.close()
