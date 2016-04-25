# Mininet-MutipathTCP
Mininet using Multipath TCP

Topology file to create a virtual network inside mininet environment as shown below: 

                  h1 ------  s1 ----------- h2
                  |                         | 
                  |--------- s2 ------------|  

The MPTCP Kernel enable the hosts to utilize the two paths simultaneously, hence achieving higher throughput from the available link bandwidth. Each link bandwidth can be varied (e.g. 10Mbps or 100Mbps). The two hosts are connected with eachother using two switches on different subnets.

Pre-requesite are:

1. MPTCP Kernel-3.18 (http://multipath-tcp.org/pmwiki.php/Users/AptRepository) running on Ubuntu 14.04 and enabled using (sudo sysctl -w net.mptcp.mptcp_enabled=1)

2. An OpenFlow based Controller running remotely (IP=127.0.0.1, Port=6653)


