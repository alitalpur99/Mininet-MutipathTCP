#!/bin/bash

ovs-ofctl snoop s1 --timestamp 2> swtich1 &

ovs-ofctl snoop s2 --timestamp 2> swtich2 &
