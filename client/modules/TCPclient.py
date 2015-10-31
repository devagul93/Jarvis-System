# TCP client example
import socket
def grab_input():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.163", 5000))
    print "connected"
    data = client_socket.recv(512)
    lim = len(data)
    data = data[:lim-1]
    print "RECIEVED:" , data
    client_socket.close()
    return data


def send_out(text):  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.163", 5000))
    print "connected"
    client_socket.send(text)
    client_socket.close()
    return
