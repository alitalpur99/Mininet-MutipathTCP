#!/usr/bin/python

'''print the timestamps and checksum for the packet-in messages of Switch S1/S2'''


from itertools import islice
timestamps=[]
mins1=[]
sec1=[]
sec1_diff=[]
mins1_diff=[]
chksum1=[]
i=0

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
					wfile.write("%s" %newline)	

with open('switch1-result.txt', 'r') as tfile:
	for l in tfile:
		l = l.rstrip().split(' ')
		timestamps.append(l[1])
		
		# append mins1 and seconds and checksum of packets
		mins1.append(l[1].split(":")[1])
		sec1.append(l[1].split(":")[2])
		chksum1.append(l[-1:])
	
	for d in range(len(sec1)):
		if i > 0:
			# print i
			# Calculate the difference of time (mins1 and seconds)
			mins1_diff.append('{0:.6}'.format(float(mins1[i])-float(mins1[i-1])))
			sec1_diff.append('{0:.6f}'.format(float(sec1[i])-float(sec1[i-1])))
		i+=1
# print sec1_diff
# Create and empty Time file 
open('switch1-time.txt', 'w').close()

with open('switch1-time.txt',"w+") as timef:
	for n in range(len(sec1_diff)):

		# append the file with difference of min and sec, and with checksum of packets
		timef.write(str(timestamps[n+1]) + "\t\t\t" + str( mins1_diff[n]) + ":" 
			+str(sec1_diff[n]) + "\t\t\t" + str(chksum1[n]) + "\n")
		




