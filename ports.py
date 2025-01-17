import socket
import time
import re
import subprocess

def get_active_ports():
    process = subprocess.run(['netstat', '-n'], capture_output=True)
    report = process.stdout.decode().splitlines()
    ports = set()
    for i in report[4:]:
        ports.add(re.split(':(?!.*:)', re.split('\s+', i)[2])[1]) 
    return ports

print(get_active_ports())
time.sleep(1)

###########################################################################
# Checking if specific ports are open or closed
###########################################################################
def check_port(host, port):
    socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result=socket_obj.connect_ex((host,port))
    socket_obj.close()
    return result==0

host="localhost"
ports=[22,80,443]

# for port in ports:
for port in range(65535):
    if check_port(host,port):
        print(f"Port {port} is open on {host}.")
    else:
        print(f"Port {port} is closed on {host}.")
