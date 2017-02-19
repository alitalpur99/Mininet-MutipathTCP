# iperf UDP Multicast on Mininet
### iperf server h3
### iperf client h1 and h2
### data transmission from h1 and h2 to server h3


### Start Mininet using Tree topology with three hosts and a single switch
sudo mn --topo tree,1,3

mininet> xterm h1 h2 h3

### start iperf server h3
h3> iperf -s -B 10.0.0.3 -u -i 1

### add route and start client at h2
h2> route add -host h2-eth0 10.0.0.3

h2> iperf -c 10.0.0.3 -u -i1 -f m -t 20

### add route and start client at h1
h1> route add -host h1-eth0 10.0.0.3

h1> iperf -c 10.0.03 -u -i1 -f m -t10

