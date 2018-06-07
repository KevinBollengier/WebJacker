import dns.resolver
import socket


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


def simple_portscan(ip: str, port_range: int):
    """
    Simple portscan to see if a port is open
    :param ip: ip address of the website to be scanned
    :param port_range: max ports to be scanned
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(1, int(port_range)):
        s.settimeout(10)
        rcode = s.connect_ex((ip, port))
        s.settimeout(None)
        if rcode == 0:
            print('[*]\tPort {port}: Open.'.format(port=port))
    s.close()
