from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sendp


def main():
    frame = Ether(dst="15:16:89:fa:dd:09")/IP(dst="9.16.5.4")/TCP()/"This is my payload"
    print(frame)
    sendp(frame)


if __name__ == '__main__':
    main()
