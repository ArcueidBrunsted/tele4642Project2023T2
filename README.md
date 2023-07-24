# tele4642Project2023T2
# generator.py randomly creates a csv file containing fake network traffic statistics.
# dashboard.py gives a WebUI running on localhost.
# netstats.csv consists of 4 columns: ['Source','Type','Destination','Size'] -> ['src_ip_addr','Protocol','dst_ip_addr','# of bytes'] ?


# project_topo.py creates the Linear topology with one switch and two hosts.
# project_controller.py is the RyuController for generate flow entries by mac-address-learning.
# traffic_capture.py captures the generated TCP/UDP packets as netstats.pcap and store the info of packets to the file netstats.csv.
