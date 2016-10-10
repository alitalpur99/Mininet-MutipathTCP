#!/usr/bin/python

'''print the timestamps and checksum for the packet-in messages of Switch S1/S2'''

#	FOR SWITCH S2

from itertools import islice

timestamps=[]
mins2=[]
sec2=[]
sec2_diff=[]
mins2_diff=[]
chksum2=[]
j=0

#	FOR SWITCH S2

# Create and empty the result file
open('switch2-result.txt', 'w').close()

with open('switch2') as f:
	for line in f:
		line = line.rstrip()
		if line.startswith('2016') and 'OFPT_PACKET_IN' in line:
			line = line.strip()
			# join the next line to OFPT_PACKET_IN
			newline = line + ' '+ ''.join(islice(f,1)) 

			# check if this is packet from h1 as source port 55000
			if 'tp_src=55000' in newline: 
				with open('switch2-result.txt', 'a') as wfile:
					wfile.write("%s" %newline)	

with open('switch2-result.txt', 'r') as tfile:
	for l in tfile:
		l = l.rstrip().split(' ')
		timestamps.append(l[1])

		# append mins2 and seconds and checksum of packets
		mins2.append(l[1].split(":")[1])
		sec2.append(l[1].split(":")[2])
		chksum2.append(l[-1:])
	
	for d in range(len(sec2)):
		if d > 0:
			# print i
			# Calculate the difference of time (mins2 and sec2onds)
			mins2_diff.append('{0:.6}'.format(float(mins2[j])-float(mins2[j-1])))
			sec2_diff.append('{0:.6f}'.format(float(sec2[j])-float(sec2[j-1])))
		
	
# Create and empty Time file 
open('switch2-time.txt', 'w').close()

with open('switch2-time.txt',"w+") as timef2:
	for n in range(len(sec2_diff)):

		# append the file with difference of min and sec2, and with checksum of packets
		timef2.write(str(timestamps[n+1]) + "\t\t\t" + str(mins2_diff[n]) + ":"
		 +str(sec2_diff[n]) + "\t\t\t" + str(chksum2[n]) + "\n")		
