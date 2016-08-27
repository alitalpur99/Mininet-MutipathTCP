#!/bin/bash
# Refer: https://sandilands.info/sgordon/doc/code/iperf-serial-clients
# Run multiple iperf clients in serial, with random wait time
# between clients
# E.g.
# ---iperf---|--sleep--|---iperf---|--sleep--|---iperf---|--...



server_ip=$1; # IP address of the iperf server
shift

server_port=$1; # Port of iperf server
shift

test_time=$1; # duration of the iperf test
shift

num_tests=$1; # Number of iperf tests
shift

ave_sleep_time=$1; # Average time to sleep
shift

iperf_options="$*" # Any other iperf options

# Calculate the range for random value
# RANDOM returns value between 0 and 2^15 (about 32000)
# If want an average sleep time of 10 seconds, then
# the range should be 0 to 20. So divide the random
# number by (2^15)/20
divider=`echo 32767/2/$ave_sleep_time | bc`

# Show the start time
date

# Repeat the iperf tests
for i in `seq 1 ${num_tests}`; do
	# Select a random number between 0 and 2^15
	random_num=`echo $RANDOM`

	# Scale down to 0 to 2*ave_sleep_time
	random_sleep=`echo ${random_num}/${divider} | bc`

	# Sleep (do nothing) 
	echo "Sleeping for ${random_sleep} seconds"
	sleep ${random_sleep}
	
	# Start an iperf test
	echo "Running iperf for ${test_time} seconds"
	iperf -c ${server_ip} -p ${server_port} -t ${test_time} ${iperf_options}

done

# Show the end time (you can use it to calculate the total time)
date
