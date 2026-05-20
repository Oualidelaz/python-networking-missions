from ipaddress import ip_address
from pathlib import Path

def extractIPs():
    path = Path("file.txt")
    if path.is_file():
        IPs = []
        with open(path, "r") as f:
            content = f.readlines()
            for line in content:
                try:
                    ip_address(line.strip())
                    IPs.append(line.strip())
                except ValueError:
                    continue
            return IPs
    else:
        return "File Not Found!"
