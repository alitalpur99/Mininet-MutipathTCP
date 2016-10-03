#!/usr/bin/python

'''print the timestamps and checksum for the packet-in messages of S2'''

#	FOR SWITCH S2

import S1_get_stats
from itertools import islice
import datetime
from datetime import timedelta

timestamps=list()
iat=list()
chksum2=list()


#	FOR SWITCH S2

# Create and empty the result file
open('switch2-result.txt', 'w').close()

# Open switch file for read mode
with open('switch2') as f:
	for line in f:
		line = line.rstrip()

		# Check if the line contains Packet_in
		if line.startswith('2016') and 'OFPT_PACKET_IN' in line:
			line = line.strip()
			
			# Join the next line to OFPT_PACKET_IN
			newline = line + ' '+ ''.join(islice(f,1)) 

			# Check if this is packet from h1 as source port 55000
			if 'tp_src=55000' in newline: 

				# Create a file with lines only from H1 as source
				with open('switch2-result.txt', 'a') as wfile:
					wfile.write(str(newline))	

# Open the switch2 result file and get the time stamps
with open('switch2-result.txt', 'r') as tfile:

	for l in tfile:
		timestamps.append(l[11:23])

		l = l.rstrip().split(' ')
		chksum2.append(l[-1:])

for n in range(len(timestamps)):
		datetimeFormat = '%H:%M:%S.%f' 
		# print timestamps[n]

		if n>0:

			# Calculate the IAT at switch2
			iat.append(datetime.datetime.strptime(timestamps[n],datetimeFormat)
			 - datetime.datetime.strptime(timestamps[n-1],datetimeFormat))
			
	
# Create and empty Time file 
open('switch2-time.txt', 'w').close()

# Save timestamps, IAT and checksum of switch2 in a file
with open('switch2-time.txt',"w+") as timef2:

	for n in range(len(timestamps)-1):
		
		data = str(timestamps[n+1]) + " " + str(iat[n]) + " " + str(chksum2[n+1]) + ("\n")
		data=data.split(' ')

		timef2.write('{0[0]:15}{0[1]:20}{0[2]:>40}'.format(data))
		
########################################################
#Calculation of ONE WAY DELAY (between Switch1 - to - Swithc2)

time1=list()
time2=list()
delay=list()

# Open the switch1 time file, and append the time
with open('switch1-time.txt','r') as tf1:
	for l in tf1:
		l=l.split(" ")
		# print l[3]
		# print len(l)
		time1.append(l[0])

# Open the switch2 time file, and append the timestamps
with open('switch2-time.txt','r') as tf2:
	for m in tf2:
		m=m.split(" ")
		time2.append(m[0])

# Create and empty the One way delay file for switch2
open('switch2-delay.txt','w').close()

with open('switch2-delay.txt','w+') as df:
	datetimeFormat = '%H:%M:%S.%f' 
	# print len(time1), len(time2)
	for n in range(len(time1)-1):

		# Calculate the One-way Delay
		delay.append(datetime.datetime.strptime(time2[n], datetimeFormat) - datetime.datetime.strptime(time1[n],datetimeFormat))
		# print delay
		df.write(str(delay) + '\n')
		

# Create an empty file, to append Timesatmps, Checksum, IAT and One-way delay
open('switch2-all.txt','w').close()

with open('switch2-all.txt','w+') as cf:
	
	cf.write('S1-time' + '\t\t' + 'S2-time' + '\t\t\t' + 'IAT-S2'+'\t\t\t'+'Delay-S2'+'\t\t' 
		+ 'S1-chksum'+'\t\t\t\t'+'S2-chksum'+ '\n')
	for n in range(len(time1)-2):
		# if S1_get_stats.chksum1[n] == chksum2[n]:

		# data = n.split(" ")
		# print '{0[0]:>15}{0[1]:>50}'.format(data)

		data = str(time1[n+1])+ " " + str(time2[n+1]) + " " + str(iat[n+1]) + " " +  str(delay[n+1]) + " " +  str(S1_get_stats.chksum1[n+2]) + " " + str(chksum2[n+2]) + ("\n")
		data=data.split(' ')
		cf.write('{0[0]:15}{0[1]:15}{0[2]:35}{0[3]:25}{0[4]:25}{0[5]:>25}'.format(data))
		

		# cf.write(str(time1[n]) + '\t'  + str(time2[n]) + '\t' + str(iat[n]) + '\t' + + '\t'
		# 	+'\t'+ '\t\t' + str(chksum2[n])+'\n')



