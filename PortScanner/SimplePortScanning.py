import socket
from IPy import IP


def scan_port(ipaddress,port):
    try:
        sock= socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        print("Port " + str(port) + " is Open for " + str(ipaddress))
    except:
        print("Port " + str(port) + " is Closed for " + str(ipaddress))

Ipaddress = input("Enter an IP Address : ")
if(Ipaddress.isdigit()):
    Port_Range = input("Enter Port Range (Example 80-443): ")
    SplitPorts = Port_Range.split("-")
    starting_port = int(SplitPorts[0])
    ending_port   = int(SplitPorts[1])

    for port in range(starting_port,ending_port):
        scan_port(Ipaddress,port)
else:
    print("Error: Enter a valid IP Address")
