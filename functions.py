import dns.resolver
import requests
import typing
from socket import *
from typing import *
from DBFunctions import DBFunctions


def get_info(file, url: str):
    output = open(file, 'a')
    r = requests.get(url="http://" + url)
    output.write('# W3bJ4ck3r Report -' + url + '\n')
    output.write('## General information'+'\n')
    output.write('\tURL : ' + url + '\n')
    output.write('\tStatus Code: ' + str(r.status_code) + '\n')
    output.close()


def verify_https(file, url: str):
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
    output.close()


def get_headers(file, url: str):
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
        pass


def dns_dump(url, record):
    """
    Function that queries DNS records based on url and the type of record provided in the parameters
    :param url: the url that needs to be queried
    :param record: Type of DNS record to query
    """
    try:
        cname_records = dns.resolver.query(url, record)
        for cname_record in cname_records:
            return "\t{dns_record} : ".format(dns_record=record) + str(cname_record)
    except dns.resolver.NoAnswer:
        return "\t{dns_record} : No information.".format(dns_record=record)
    except dns.resolver.NoNameservers:
        return "\tShit happened."


def simple_portscan(url):
    """
    Simple portscan to see if a port is open
    :param url: host to be scanned
    :return List of strings containing open ports.
    """
    remote_host_ip = gethostbyname(url)
    db_functions = DBFunctions()
    ports_services = db_functions.get_ports()
    print("Scanning: " + str(remote_host_ip))
    open_ports = []
    for (port, service) in ports_services:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.05)
        result = s.connect_ex((remote_host_ip, port))
        if result == 0:
            open_ports.append("Port {port}: \t open    {service}".format(port=port, service=service))
        s.close()
    return open_ports


def print_to_md_file(text: List[str]):
    file = open("test.md", "w")
    for line in text:
        file.write(line+"\n")
    file.close()
    pass
