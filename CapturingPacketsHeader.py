import pcapy
import struct


def main():
    cap = pcapy.open_live('en0', 65535, 1, 0)

    while True:
        (header, payload) = cap.next()
        ethernet_header = payload[:14]  # byte 0 -14

        src_mac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
            ethernet_header[0], ethernet_header[1], ethernet_header[2], ethernet_header[3], ethernet_header[4], ethernet_header[5])
        dest_mac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
            ethernet_header[6], ethernet_header[7], ethernet_header[8], ethernet_header[9], ethernet_header[10],
            ethernet_header[11])

        print("Source MAC: {} Destination MAC: {}".format(src_mac, dest_mac))

        ip_header = struct.unpack('!BBHHHBBH4s4s', payload[14:34]) # IP header is 20 bytes long
        time_to_live = ip_header[5]
        protocol = ip_header[6]

        print("Protocol {} Time To Live {}".format(protocol, time_to_live))


if __name__ == '__main__':
    main()
