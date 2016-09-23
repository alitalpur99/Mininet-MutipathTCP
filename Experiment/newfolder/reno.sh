#!/bin/bash

# set tcp reno as congestion control
sysctl -w net.ipv4.tcp_co ngestion_control=reno

# set tcp auto-tunning off
sysctl -w net.ipv4.tcp_moderate_rcvbuf=0

#tcp window scaling off
sysctl -w net.ipv4.tcp_window_scaling=0

#python Topo-24.py

