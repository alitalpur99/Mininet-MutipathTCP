'''2 host and 2 switch topo to check the cwnd graphs, and timings
delay is only added between the switches to avoid timing/delay generator ambuity while observing it in wireshark'''

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
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	# s3 = net.addSwitch('s3')



	net.addLink(h1, s1, intfName1='h1-eth2', intfName2='s1-eth1',bw=100)#,bw=100, max_queue_size=1000, delay='5ms')
	net.addLink(s1, s2, intfName1='s1-eth2', intfName2='s2-eth2',bw=100, delay='40ms')#, max_queue_size=20)
	net.addLink(h2, s2, intfName1='h2-eth2', intfName2='s2-eth1',bw=100)

	print "*** Starting network"
	net.build()

	s1.start('')
	s1.cmd('switch s1 start')
	s2.start('')
	s2.cmd('switch s2 start')
	# s3.start('')
	# s3.cmd('switch s3 start')

	# add flows in switch
	s1.cmd('ovs-ofctl add-flow s1 in_port=2,actions:output=1')
	s1.cmd('ovs-ofctl add-flow s1 in_port=1,actions:output=2')
	s2.cmd('ovs-ofctl add-flow s2 in_port=2,actions:output=1')
	s2.cmd('ovs-ofctl add-flow s2 in_port=1,actions:output=2')
	# s3.cmd('ovs-ofctl add-flow s3 in_port=2,actions:output=1')
	# s3.cmd('ovs-ofctl add-flow s3 in_port=1,actions:output=2')
	
	# h1.cmd('h1 ping h2 -c 2')

	# h2.cmd('tcpdump -i h2-eth2 -w server-tcpdump')
	# h1.cmd('tcpdump -i h1-eth2 -w client-tcpdump')
	# h2.cmd('iperf -s > server_output.txt &')
	# h1.cmd('iperf -c ', h1.IP() + ' -i 1 -t 50   >  client_output.txt &')

	print "*** Running CLI"
	CLI( net )
	print "*** Stopping network"
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	topology()
