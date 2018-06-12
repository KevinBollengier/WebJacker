import dns.resolver
from socket import *
from typing import *
from port_list import PortList


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
    :param port_range: max ports to be scanned
    :return List of strings containing open ports.
    """
    # TODO Multithreading for performance
    remote_host_ip = gethostbyname(url)
    port_list = PortList()
    port_dict = port_list.get_port_dict()
    print("Scanning: " + str(remote_host_ip))
    open_ports = []
    for port, service in port_dict.items():
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
