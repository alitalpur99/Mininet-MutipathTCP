#!/usr/bin/python

'''print the timestamps, IAT and checksum for the packet-in messages of Switch S1'''


from itertools import islice
import datetime
from datetime import timedelta

timestamps=list()
mins1=list()
mins1_diff=list()
sec1=list()
sec1_diff=list()
chksum1=list()
iat=list()

#	FOR SWITCH S1

# Create and empty the result file
open('switch1-result.txt', 'w').close()

with open('switch1') as f:
	for line in f:
		line = line.rstrip()
		if line.startswith('2016') and 'OFPT_PACKET_IN' in line:
			line = line.strip()
			# join the next line to OFPT_PACKET_IN
			newline = line + ' '+ ''.join(islice(f,1)) 

			# check if this is packet from h1 as source port 55000
			if 'tp_src=55000' in newline: 
				with open('switch1-result.txt', 'a') as wfile:
					wfile.write(str(newline))

with open('switch1-result.txt', 'r') as tfile:

	for l in tfile:
		timestamps.append(l[11:23])
		l = l.rstrip().split(' ')
		chksum1.append(l[-1:])
	for n in range(len(timestamps)):
		datetimeFormat = '%H:%M:%S.%f' 
		# print timestamps[n]
		if n>0:

			# Calculate the IAT at switch1
			# print (datetime.datetime.strptime(timestamps[n],datetimeFormat)- datetime.datetime.strptime(timestamps[n-1],datetimeFormat))
			iat.append(datetime.datetime.strptime(timestamps[n],datetimeFormat) - datetime.datetime.strptime(timestamps[n-1],datetimeFormat))
# print str(iat)

# Create and empty Time file 
open('switch1-time.txt', 'w').close()

# Save timestamps, IAT and checksum of switch1 in a file
with open('switch1-time.txt',"w+") as timef:
	
	for n in range(len(timestamps)-1):
		
		data = str(timestamps[n+1]) + " " + str(iat[n]) + " " + str(chksum1[n+1]) + ("\n")
		data=data.split(' ')

		timef.write('{0[0]:15}{0[1]:20}{0[2]:>40}'.format(data))
		