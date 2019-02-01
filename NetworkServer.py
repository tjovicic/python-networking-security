import socket


def main():
    size = 512
    host = ''
    port = 9898

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((host, port))
    sock.listen(5)

    c, addr = sock.accept()
    data = c.recv(size)
    if data:
        print("connection from {} : {}".format(addr[0], data.decode('utf-8')))

    sock.close()


if __name__ == '__main__':
    main()
