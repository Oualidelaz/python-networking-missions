from ipaddress import ip_address

def isPrivateIP(ip):
    if ip_address(ip).is_private:
        return True
    return False
