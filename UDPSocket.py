import socket

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b"Hi, this is a message", ("localhost", 5599))
    except Exception as e:
        print("exception" + e)


if __name__ == '__main__':
    main()
