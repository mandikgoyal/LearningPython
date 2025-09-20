import socket
from IPy import IP
import ipaddress as ip


def scan(tagerts):
    print("[0_T] Scanning for " + tagerts)
    actualip=check_ip(tagerts)
    for port in range(20,100):
        scan_port(actualip,port)

def check_ip(input):
    try:
        IP(input)
        return input
    except ValueError:
        return socket.gethostbyname(input)
    
def scan_port(ipaddress,port):
    try:
        sock= socket.socket()
        sock.settimeout(1.0)
        sock.connect((ipaddress,port))
        try:
            print("[+] Port " + str(port) + " is Open for " + str(ipaddress) + " for" + banner)
        except:
            print("[+] Port " + str(port) + " is Open for " + str(ipaddress))
    except:
            pass

userinputs = input("Enter Multiple IP Addresses / Domains : ")

if "," in userinputs:
    for target in userinputs.split(","):
        scan(target.strip(" ").strip("http://").strip("https://"))
else :
        scan(userinputs)