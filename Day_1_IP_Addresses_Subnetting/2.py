from ipaddress import ip_address, IPv4Address

def is_validIP(ip):
    try:
        return "IPv4" if type(ip_address(ip)) is IPv4Address else "IPv6"
    except Exception:
        return "Invalid"


def IPcnv(ip):
    if is_validIP(ip) == "IPv4":
        result = []
        s = ip.split('.')
        for chunck in s:
            binary = bin(int(chunck))[2:]
            result.append(binary.zfill(8))
        return '.'.join(result)
    else:
        return f"Invalid IP: {ip}"


if __name__ == "__main__":
    print(IPcnv('198.168.100.98'))