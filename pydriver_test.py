import pydivert

# Capture only TCP packets to port 80, i.e. HTTP requests.  tcp.DstPort == 6900 or tcp.DstPort == 54400
bing_bing = [
    b'\x07\x00a\x03\x00\x00\x06',
    b'\x07\x00a\x03\x00\x00\x05',
    b'\x07\x00a\x03\x00\x00\x04',
    b'\x07\x00a\x03\x00\x00\x03',
    b'\x07\x00a\x03\x00\x00\x02',
    b'\x07\x00a\x03\x00\x00\x01',
    b'\x07\x00a\x03\x00\x00\x00',
]
counter = 0
while True:
    with pydivert.WinDivert("tcp.DstPort == 6900 or tcp.DstPort == 10001 and tcp.PayloadLength > 0") as w:
        for packet in w:
            # print(packet)
            # msg = "poring"

            if packet.is_inbound:
                print(f"Inbound: {packet.payload}")
            else:
                print(f"Outbound: {packet.payload}")

                # if 'Marytes' in str(packet.payload):
                #     msg = input('Message: ')
                #     length = 10 + len(msg)
                #     message = fr"\x{length}\x00\x8c\x00\x{length - 2}\x00Marytes : {msg}"
                #     message = str.encode(message)
                #     message = message.decode('unicode-escape').encode('ISO-8859-1')
                #     packet.payload = message

            # try:
            #     packet.payload = bing_bing[counter]
            #     counter += 1
            # except IndexError:
            #     counter = 0
            #     packet.payload = bing_bing[counter]

            # print(print('_'.join([str(_) for _ in packet.payload])))
            # packet.payload = b'\x07\x00_\x039\x85\x80'
            # print(packet.payload)
            #
            # packet.dst_addr = '127.0.0.1'
            # packet.dst_port = 6901
            #
            # packet.ipv4.dst_addr = '127.0.0.1'q
            # packet.tcp.dst_port = 6901
            # print(packet.dst_addr, packet.dst_port)
            w.send(packet)
