#!/bin/bash

# Flow tables for 2switch or 4switch configuration

# FLOW TABLE FOR 2S-4H TOPO

sh ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:3
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3,controller

sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:1
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:1
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:1


sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:3
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:3

sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2


sh ovs-ofctl add-flow s2 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:3
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:3
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:2

sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:1
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:1
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:1

sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:3
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:3

sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:2,controller
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:2



# FLOW TABLE FOR 4S-4H TOPO

sh ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:2
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:2,controller

sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:1
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:1
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:1


sh ovs-ofctl add-flow s2 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:3
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:3

sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:1
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:3

sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:1
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:2

sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:1


sh ovs-ofctl add-flow s3 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:3

sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:1
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3

sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:1
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:3



sh ovs-ofctl add-flow s4 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:2

sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:1,controller
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:1
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:1





#NOT WORKING

sh ovs-ofctl add-flow s1 idle_timeout=10,priority=1,in_port=1,actions=output:2
sh ovs-ofctl add-flow s1 idle_timeout=10,priority=1,in_port=2,actions=output:1
sh ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:2
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:1
sh ovs-ofctl add-flow s1 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.1,actions=output:2
sh ovs-ofctl add-flow s1 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.4,actions=output:1



sh ovs-ofctl add-flow s2 idle_timeout=10,priority=1,in_port=1,actions=output:3
sh ovs-ofctl add-flow s2 idle_timeout=10,priority=1,in_port=3,actions=output:1
sh ovs-ofctl add-flow s2 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:3
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:1
sh ovs-ofctl add-flow s2 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.2,actions=output:3
sh ovs-ofctl add-flow s2 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.3,actions=output:1

sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3
sh ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s2 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.1,actions=output:3
sh ovs-ofctl add-flow s2 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.4,actions=output:2



sh ovs-ofctl add-flow s3 idle_timeout=10,priority=1,in_port=1,actions=output:2
sh ovs-ofctl add-flow s3 idle_timeout=10,priority=1,in_port=2,actions=output:1
sh ovs-ofctl add-flow s3 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:03,actions=output:1
sh ovs-ofctl add-flow s3 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.3,actions=output:2
sh ovs-ofctl add-flow s3 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.2,actions=output:1
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s3 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.1,actions=output:3
sh ovs-ofctl add-flow s3 idle_timeout=180,priority=33005,dl_type=0x800,nw_src=10.0.0.4,actions=output:2




sh ovs-ofctl add-flow s4 idle_timeout=10,priority=1,in_port=1,actions=output:2
sh ovs-ofctl add-flow s4 idle_timeout=10,priority=1,in_port=2,actions=output:1
sh ovs-ofctl add-flow s4 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:1
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s4 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.1,actions=output:1
sh ovs-ofctl add-flow s4 idle_timeout=180,priority=33001,dl_type=0x800,nw_src=10.0.0.4,actions=output:2


