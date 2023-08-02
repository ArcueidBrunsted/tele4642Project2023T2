from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections, irange
import time


class ProjectTopo(Topo):
    def __init__(self, *args, **params):
        super(ProjectTopo, self).__init__(*args, **params)

    def build(self):
        s = self.addSwitch('s1')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        self.addLink(s, h1, port1=1, port2=1, cls=TCLink, bw=10)
        self.addLink(s, h2, port1=2, port2=1, cls=TCLink, bw=10)

    def run_iperf(self, type, client, server, duration):
        if type == "TCP":
            server.cmd(f'iperf -s &')
            time.sleep(0.5)
            client.cmd(f"iperf -c {server.IP()} -t {duration}")
            server.sendInt()  # Stop TCP server
        else:
            server.cmd(f'iperf -u -s &')
            time.sleep(0.5)
            client.cmd(f"iperf -u -c {server.IP()} -t {duration}")
            server.sendInt()  # Stop UDP server


def TopoStart():
    topo = ProjectTopo()
    c1 = RemoteController("RyuController", ip="127.0.0.1",
                          port=6653, protocols="OpenFlow13")
    net = Mininet(topo=topo, link=TCLink, controller=c1,
                  autoSetMacs=True, autoStaticArp=True)

    net.start()
    dumpNodeConnections(net.hosts)

    h1, h2 = net.get('h1', 'h2')
    # print(ip_addr_h1)
    duration = 2

    # Start TCP traffic Generation
    topo.run_iperf("TCP", h1, h2, duration)
    time.sleep(2)
    # Start TCP traffic Generation
    topo.run_iperf("UDP", h1, h2, duration)
    time.sleep(2)

    CLI(net)
    net.stop()


if __name__ == "__main__":
    setLogLevel('info')
    TopoStart()

topos = {"projectTopo": (lambda: ProjectTopo())}
