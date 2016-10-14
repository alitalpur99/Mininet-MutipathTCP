'''
CHANGE THE ORIGINAL WIRESHARK FILE TO ONLY DISPLAY THE NO, TIME & INFO COLUMNS
'''


import datetime
from datetime import timedelta



"""FOR SENDER H1, TAKE THE TIME VALUES"""

i1=0
count1=0
fields1=[]
time1=[]
with open('h1dump.txt','r') as f1:
	for line in f1:
		i1=i1+1
		line=line.split()
			
		# print line[5]
		if line[3]=='10.0.0.1':# and :
		# 	# line=line[4:]
			if line[5]=='55000' or line[7]=='55000'  or line[8]=='55000' or line[9]=='55000':
				# print line[1]
		 		time1.append(line[1])
		 		fields1.append(line[5:])
# 		# 		# print line
				count1 = count1+1
		## if i1>100: break
# # # # 			if line[6]=='55000':

print count1 #82660



# # ############################# # ############################


"""FOR RECEIVER H4, TAKE TIME VALUES"""
i2=0
count2=0
time2=[]
fields2=[]
with open('h4dump.txt','r') as f2:
	for line in f2:
		i2=i2+1
		line=line.split()
			
		if line[3]=='10.0.0.1':# and :
		# 	# line=line[4:]
		# 	# print line
			if line[5]=='55000' or line[7]=='55000'  or line[8]=='55000' or line[10]=='55000':
				# print line[4]
		 		time2.append(line[1])
		 		fields2.append(line[4:])
		# 		# print line
				count2 = count2+1
		# if i==110: break
# # # 			if line[6]=='55000':
print count2 # 82569


# # ############################# # ############################

"""SAVE TO A FILE, LINES OF SENDER AND RECEIVER DUMPS"""

open('h1h4','w').close()

with open('h1h4','w+') as file:
	
	for n in range(len(time2)):
		# print 'H1',time1[n], fields1[n]
		# print 'H4',time2[n], fields2[n]
		file.write('H4'+' '+str(time2[n])+' '+str(fields2[n]))
		file.write('\n')
		file.write('H1'+' '+str(time1[n])+' '+ str(fields1[n]))
		file.write('\n')


# # ############################# # ############################

"""CREATE A FILE WITH TIME AND (H4-H1 DIFF = ONE-WAY DELAY)"""

open('tcpdump-timedelay','w').close()
with open('tcpdump-timedelay','w+') as file:

	datetimeFormat = '%H:%M:%S.%f'
	total=0
	for n in range(len(time2)):
		t=str(time1[n])

		t.split(":")
		sec=t[6:]
		time_diff = datetime.datetime.strptime(time2[n], datetimeFormat) - datetime.datetime.strptime(time1[n],datetimeFormat)
		# print time_diff
		one_way_delay=str(time_diff)
		one_way_delay=one_way_delay.split(":")[2]

		if n<10418:
			# print sec
			file.write(str(sec)+" "+str(one_way_delay))
			file.write('\n')
		
		else:
			# print total
	
			file.write(str(total)+" "+str(one_way_delay))
			file.write('\n')

		# when first time 59.99 sec achieved add 60 to it
		if n>10418: 
			total=float(sec)+60
		
		
			# when second time 59.99 is reached, add 120 to it
			if n>59941:
				total=float(sec)+120