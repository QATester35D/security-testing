import socket

def check_port(host, port):
    socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result=socket_obj.connect_ex((host,port))
    socket_obj.close()
    return result==0

host="localhost"
ports=[22,80,443]

for port in ports:
    if check_port(host,port):
        print(f"Port {port} is open on {host}.")
    else:
        print(f"Port {port} is closed on {host}.")