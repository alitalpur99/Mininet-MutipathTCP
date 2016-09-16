#!/bin/bash

# set tcp reno as congestion control
sysctl -w net.ipv4.tcp_congestion_control=reno

# set tcp auto-tunning off
sysctl -w net.ipv4.tcp_moderate_rcvbuf=0

#tcp window scaling off
sysctl -w net.ipv4.tcp_window_scaling=1

#python Topo-24.py
