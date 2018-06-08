import dns.resolver
from socket import *


def dns_dump(url: str, record: str):
    """
    Function that queries DNS records based on url and the type of record provided in the parameters
    :param url: the url that needs to be queried
    :param record: Type of DNS record to query
    """
    try:
        cname_records = dns.resolver.query(url, record)
        for cname_record in cname_records:
            print("\t{dns_record} : ".format(dns_record=record) + str(cname_record))
    except dns.resolver.NoAnswer:
        print("\t{dns_record} : No information.".format(dns_record=record))


def simple_portscan(url, port_range: int):
    """
    Simple portscan to see if a port is open
    :param url: host to be scanned
    :param port_range: max ports to be scanned
    """
    # TODO Multithreading for performance
    # TODO make port_range dynamic
    # TODO map ports to relating services in output
    remote_host_ip = gethostbyname(url)
    print("Scanning: " + str(remote_host_ip))
    for port in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.05)
        result = s.connect_ex((remote_host_ip, port))
        if result == 0:
            print("[*]\tPort {port}: OPEN".format(port=port))
        s.close()
