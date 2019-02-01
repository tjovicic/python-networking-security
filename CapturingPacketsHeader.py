import pcapy
import struct


def main():
    cap = pcapy.open_live('en0', 65535, 1, 0)

    while True:
        (header, payload) = cap.next()
        l2hdr = payload[:14]

        print(l2hdr)
        l2data = struct.unpack("!6s6sH", l2hdr)

        src_mac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[0]), ord(l2hdr[1]), ord(l2hdr[2]), ord(l2hdr[3]), ord(l2hdr[4]), ord(l2hdr[5]))
        dest_mac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[6]), ord(l2hdr[7]), ord(l2hdr[8]), ord(l2hdr[9]), ord(l2hdr[10]), ord(l2hdr[11]))
        print("Source MAC: {} Destination MAC: {}".format(src_mac, dest_mac))

if __name__ == '__main__':
    main()
