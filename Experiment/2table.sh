#!/bin/bash

sysctl -w net.ipv4.tcp_congestion_control=reno

ovs-ofctl del-flows s1
ovs-ofctl del-flows s2


ovs-ofctl add-flow s1 in_port=1,actions=output:2,controller
ovs-ofctl add-flow s1 in_port=2,actions=output:1

ovs-ofctl add-flow s2 in_port=2,actions=output:1,controller
ovs-ofctl add-flow s2 in_port=1,actions=output:2

t=$(date +%b%d-%H:%M)
filename1=S1-"$t".txt
filename2=S2-"$t".txt
# touch /home/ali/pox\ understanding/2host/"$filename1"
# touch /home/ali/pox\ understanding/2host/"$filename1"


ovs-ofctl snoop s1 --timestamp > /home/ali/pox\ understanding/2host/"$filename1" 2>&1 &
ovs-ofctl snoop s2 --timestamp > /home/ali/pox\ understanding/2host/"$filename2" 2>&1 &
