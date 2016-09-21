#!/bin/bash

tcpdump -i h1-eth0 -w h1 &

iperf3 -c 10.0.0.4 -B 10.0.0.1 --cport 55000 -t100 -i1 > iperf3h1.txt
