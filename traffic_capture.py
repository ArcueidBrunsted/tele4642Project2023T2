import pyshark
import csv


class Traffic():
    def __init__(self) -> None:
        pass

    def capture_traffic(self, time_sniff, interface):
        traffic_out = "netstats.pcap"  # Output PCAP file
        with open(traffic_out, "w+"):
            capture = pyshark.LiveCapture(
                interface=interface, output_file=traffic_out)
            # Sniffing traffic with the time period as time_sniff
            capture.sniff(timeout=time_sniff)

        return traffic_out

    def packet_info_extraction(self, packet):
        try:
            # Info for TCP/UDP packets
            protocol = packet.transport_layer
            source_address = packet.ip.src
            source_port = packet[packet.transport_layer].srcport
            destination_address = packet.ip.dst
            destination_port = packet[packet.transport_layer].dstport
            packet_length = packet.captured_length

            return (source_address, protocol, destination_address, packet_length)
            # return (f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port} with length {packet_length}')
        except AttributeError as e:
            pass

        return None

    def packet_handling(self, traffic_pcap):
        # Convert the PCAP to readable packets
        capture = pyshark.FileCapture(traffic_pcap)
        file_name = traffic_pcap.replace(".pcap", ".csv")

        with open(file_name, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            header = ["src_ip_addr", "Protocol", "dst_ip_addr", "# of bytes"]
            writer.writerow(header)

            for packet in capture:
                res = self.packet_info_extraction(packet)
                if res:
                    writer.writerow(res)
                else:
                    continue


if __name__ == "__main__":
    traffic = Traffic()
    capture = traffic.capture_traffic(15, "s1-eth1")  # 15s for sniffing with interface as s1-eth1 
    traffic.packet_handling(capture)

