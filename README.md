# tele4642Project2023T2

## To run the program, using the following steps:

1. Start the Controller `project_controller.py`.

````shell
ryu-manager project_controller.py
````

2. Start the Topology `project_topo.py`.

````shell
sudo python3 project_topo.py 
````

3. Running the capture & parsing program `traffic_capture.py`.  Remember the time interval between running the program and starting the Topology should not be too long.

````shell
sudo python3 traffic_capture.py
````

4. Running the `dashboard.py` to get the statistic of TCP/UDP packets.

````shell
sudo python3 dashboard.py
````



## The function of the programs are listed below:

 1. generator.py randomly creates a csv file containing fake network traffic statistics.

 2. dashboard.py gives a WebUI running on localhost.
 3. netstats.csv consists of 4 columns: ['Source','Type','Destination','Size'] -> ['src_ip_addr','Protocol','dst_ip_addr','# of bytes'] ?


 4. project_topo.py creates the Linear topology with one switch and two hosts.
 5. project_controller.py is the RyuController for generate flow entries by mac-address-learning.
 6. traffic_capture.py captures the generated TCP/UDP packets as netstats.pcap and store the info of packets to the file netstats.csv.
