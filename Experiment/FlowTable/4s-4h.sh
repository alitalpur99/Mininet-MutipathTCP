#!/bin/bash

# 4switch 4host flow table configuration


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

sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:1


sh ovs-ofctl add-flow s4 dl_type=0x806,nw_proto=1,action=flood
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:2

sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:1,controller
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:1
sh ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:1
