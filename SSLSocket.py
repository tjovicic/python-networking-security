import ssl
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_socket = ssl.wrap_socket(s)

    try:
        ssl_socket.connect(('www.google.com', 443))
        print(ssl_socket.cipher())
    except Exception as e:
        print("Connection error {}".format(e))

    try:
        ssl_socket.write(b"GET / \r\n")
    except Exception as e:
        print("Write error {}".format(e))

    data = None
    try:
        data = ssl_socket.read()
    except Exception as e:
        print("Read error {}".format(e))

    print(data.decode('utf-8'))


if __name__ == '__main__':
    main()
