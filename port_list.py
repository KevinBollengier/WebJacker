class PortList:
    """
    Class that instances a list of commonly used ports.
    Used for scanner in functions.py
    """
    def __init__(self):
        self.ports_dict = {
            20: 'FTP',
            21: 'FTP Control',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            67: 'DHCP Server',
            68: 'DHCP Client',
            69: 'TFTP',
            80: 'HTTP',
            110: 'POP3',
            119: 'NNTP',
            123: 'NTP',
            137: 'NetBIOS Name Service',
            138: 'NetBIOS Datagram Service',
            139: 'Netbios Session Service',
            143: 'IMAP',
            161: 'SNMP',
            162: 'SNMP-trap',
            389: 'LDAP',
            443: 'HTTPS',
            445: 'SMB',
            465: 'SMTP',
            546: 'DHCP Client (ipv6)',
            547: 'DHCP Server (ipv6)',
            569: 'MSN',
            587: 'SMTP',
            990: 'FTPS',
            993: 'IMAP',
            995: 'POP3',
            1080: 'SOCKS proxy',
            1194: 'OpenVPN',
            3306: 'MySQL',
            3389: 'RDP',
            3689: 'DAAP',
            5432: 'PostgreSQL',
            5800: 'VNC',
            5900: 'VNC',
            6346: 'Gnutella',
            8080: 'HTTP'
        }

    def get_port_dict(self):
        return self.ports_dict
