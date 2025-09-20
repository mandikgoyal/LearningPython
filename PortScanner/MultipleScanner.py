import socket
from IPy import IP
import ipaddress as ip

def scan(tagerts,starting_port,ending_port):
    actualip=check_ip(tagerts)
    for port in range(starting_port,ending_port):
        scan_port(actualip,port)

def check_ip(input):
    print(input)
    try:
        IP(input)
        return input
    except ValueError:
        return socket.gethostbyname(input)

def scan_port(ipaddress,port):
    try:
        sock= socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        print("[+] Port " + str(port) + " is Open for " + str(ipaddress))
    except:
        pass

userinputs = input("Enter Multiple IP Addresses / Domains : ")
Port_Range = input("Enter Port Range (Example 80-443): ")
SplitPorts = Port_Range.split("-")
starting_port = int(SplitPorts[0])
ending_port   = int(SplitPorts[1])
if "," in userinputs:
    for target in userinputs.split(","):
        scan(target.strip(" "),starting_port,ending_port)
else :
        scan(userinputs,starting_port,ending_port)