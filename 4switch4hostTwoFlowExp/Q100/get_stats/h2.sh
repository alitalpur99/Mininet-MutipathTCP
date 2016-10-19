#!/bin/bash

tcpdump -i h2-eth0 -w h2 &

iperf3 -c 10.0.0.3 -t5 -i1 > iperf3h2.txt
