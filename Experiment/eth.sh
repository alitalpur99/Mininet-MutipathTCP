#!/bin/bash

ethtool -K h1-eth0 gro off
ethtool -K h1-eth0 gso off
ethtool -K h1-eth0 tso off


ethtool -K h2-eth0 gro off
ethtool -K h2-eth0 gso off
ethtool -K h2-eth0 tso off


ethtool -K h3-eth0 gro off
ethtool -K h3-eth0 gso off
ethtool -K h3-eth0 tso off

ethtool -K h4-eth0 gro off
ethtool -K h4-eth0 gso off
ethtool -K h4-eth0 tso off




