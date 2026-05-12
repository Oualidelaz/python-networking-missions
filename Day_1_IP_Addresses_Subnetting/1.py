from ipaddress import ip_address, IPv4Address

def is_validIP(ip):
    try:
        return "IPv4" if type(ip_address(ip)) is IPv4Address else "IPv6"
    except Exception:
        return "Invalid"
