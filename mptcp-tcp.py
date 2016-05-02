#!/usr/bin/python
"""
2 hosts (h1 h2 directly connected) via two interfaces to utilize the multipath.
iperf result show twice the bandwidth i.e. for two 100Mbps links aroung 188Mbps.

"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():
    "Create a network."
    net = Mininet( controller=None, link=TCLink, switch=OVSKernelSwitch )
    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.10.33/24' )
    s1 = net.addSwitch ( 's1')

    print "*** Creating links"

    net.addLink(h1, h2, intfName1='h1-eth0', intfName2='h2-eth0',bw=100)
    net.addLink(h1, s1, intfName1='h1-eth1', intfName2='s1-eth1', bw=100)
    net.addLink(h2, s1, intfName1='h2-eth1', intfName2='s1-eth2', bw=100)
    net.addLink(h3, s1, intfName1='h3-eth0', intfName2='s1-eth0', bw=100)
    h1.cmd('ifconfig h1-eth1 10.0.10.11/24 netmask 255.255.255.0')
    h2.cmd('ifconfig h2-eth1 10.0.10.22/24 netmask 255.255.255.0')
# h3 cant ping h2?
    print "*** Starting network"
    net.build()
    print "*** Running CLI"
    CLI( net )
    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':

    setLogLevel( 'info' )

    topology()
