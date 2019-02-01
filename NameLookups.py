import socket


def main():
    print(socket.gethostbyaddr('8.8.8.8'))
    print(socket.gethostbyaddr('www.google.com'))


if __name__ == '__main__':
    main()
