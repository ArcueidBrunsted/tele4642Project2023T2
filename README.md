# tele4642Project2023T2

## Preparation Steps:

1. Install Mininet and Ryu in Ubuntu
````shell
sudo apt install mininet
pip install ryu
````
2. Install dash, dash_raq and corrsponding dependencies for displaying the statistic
````shell
pip install dash, dash_raq
````

## A Known Issues: If the ImportError of ryu-manager raised:
````python
Traceback (most recent call last):
  File "/home/shuai/miniconda3/envs/myenv/bin/ryu-manager", line 5, in <module>
    from ryu.cmd.manager import main
  File "/home/shuai/miniconda3/envs/myenv/lib/python3.8/site-packages/ryu/cmd/manager.py", line 33, in <module>
    from ryu.app import wsgi
  File "/home/shuai/miniconda3/envs/myenv/lib/python3.8/site-packages/ryu/app/wsgi.py", line 109, in <module>
    class _AlreadyHandledResponse(Response):
  File "/home/shuai/miniconda3/envs/myenv/lib/python3.8/site-packages/ryu/app/wsgi.py", line 111, in _AlreadyHandledResponse
    from eventlet.wsgi import ALREADY_HANDLED
ImportError: cannot import name 'ALREADY_HANDLED' from 'eventlet.wsgi' (/home/shuai/miniconda3/envs/myenv/lib/python3.8/site-packages/eventlet/wsgi.py)
````

Try to use python3.8 and follow the steps:
````shell
pip install eventlet==0.30.2
````

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



## The functions of each program are listed below:

 1. generator.py randomly creates a csv file containing fake network traffic statistics.
 2. dashboard.py gives a WebUI running on localhost. It reads netstats.csv every 5 seconds and refreshes the web page.
 3. netstats.csv consists of 4 columns:['src_ip_addr','Protocol','dst_ip_addr','# of bytes'].
 4. project_topo.py creates the Linear topology with one switch and two hosts. TCP and UDP packets are generated using `iperf`
 5. project_controller.py is the RyuController for generate flow entries by mac-address-learning.
 6. traffic_capture.py captures the generated TCP/UDP packets as netstats.pcap and store the info of packets to the file netstats.csv.
