# Open netcat listener on port 5555: nc -l 5555
# and then run this script

import socket


def main():
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('localhost', 5555)
    my_sock.connect(addr)
    try:
        msg = b"hi, this is test\n"
        my_sock.sendall(msg)
    except socket.error as e:
        print(e)
    finally:
        my_sock.close()


if __name__ == "__main__":
    main()
