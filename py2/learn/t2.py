# coding: utf-8
__author__ = 'fripSide'

"""
test sockets
"""

import socket, os, time

def test_socket():
    print socket.has_ipv6
    # (family, socktype, proto, canonname, sockaddr)
    print socket.getaddrinfo("127.0.0.1", 80)


test_socket()

def echo_server():
    server = socket.socket()
    server.bind(('', 6666))
    # server.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # server.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # server.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    server.listen(5)
    conn, addr = server.accept()
    print("connected by", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall("From Server: " + data)
    conn.close()

def send_client():
    client = socket.socket()
    client.connect(('', 6666))
    for i in range(3):
        client.sendall("Hello Client -> " + str(i))
        data = client.recv(1034)
        print("Received", repr(data))
        # time.sleep(2)
    client.close()

def test_server():
    if os.fork():
        echo_server()
    else:
        send_client()

test_server()


def test_raw():
    import socket

    # the public network interface
    HOST = socket.gethostbyname(socket.gethostname())

    # create a raw socket and bind it to the public interface
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, 0))

    # Include IP headers
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # receive all packages
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    # receive a package
    print s.recvfrom(65565)

    # disabled promiscuous mode
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


# test_raw()
HOST = socket.gethostbyname(socket.gethostname())
print(HOST, socket.gethostname() )

"""
了解SO_KEEPALIVE，TCP_NODELAY参数的作用，了解设置SO_RCVBUF和SO_SNDBUF的意义
"""

