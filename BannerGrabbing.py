import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("www.microsoft.com", 80))

    http_get = b"GET / HTTP/1.1\nHost: www.microsoft.com\n\n"
    data = None

    try:
        sock.sendall(http_get)
        data = sock.recvfrom(2048)
    except socket.error as e:
        print(e)
    finally:
        sock.close()

    data = data[0].decode('utf-8')
    print(data)


if __name__ == '__main__':
    main()
