import S1_get_stats
import S2_get_stats
from datetime import datetime
import time
from datetime import timedelta

# for i in range(0,10):
# 	print S1_get_stats.chksum1[i+1], S1_get_stats.timestamps[i]

# s="13:37:25.913"
# d = datetime.strptime(s, "%H:%M:%S.%f")
# print time.mktime(d.timetuple())

for i,v in enumerate(S2_get_stats.chksum2):
	if str(S2_get_stats.chksum2[i]) in S1_get_stats.chksum1:
		print i, S2_get_stats.chksum2[i], i, S1_get_stats.chksum1[i]
	# else:
	# 	for n in range(0,100):
	# 		if str(S2_get_stats.chksum2[i])==str(S1_get_stats.chksum1[i+n]):
	# 			print i, S2_get_stats.chksum2[i], i+n, S1_get_stats.chksum1[i+n]	

# time2=[]
# with open("switch2-all.txt") as f:
# 	for l in f:
# 		l=l.strip()
# 		l=l.split("\t")
# 		time2.append(l[1])
# for i in range(len(time2)):
# 	t=time2[i]
# 	=t.split(":")
# 	print t		


# def get_sec(time_str):
#     h, m, s = time_str.split(':')
#     return int(h) * 3600 + int(m) * 60 + int(s)

# print get_sec('13:37:25')
# for n in range(len(S1_get_stats.timestamps)):
# 	get_sec(S1_get_stats.timestamps[n])





# '''comon in S1'''


# iat=[]
# time_delta=[]
# for idx, val in enumerate(S1_get_stats.chksum1):
# 	if val in S2_get_stats.chksum2:

# 		datetimeFormat = '%H:%M:%S.%f' 
# 		try:
# 			if idx>0 and val in S2_get_stats.chksum2:
# 				print S1_get_stats.timestamps[idx], idx, val, S2_get_stats.timestamps[idx], S2_get_stats.chksum2.index(val), S2_get_stats.chksum2[idx]
# 			# if idx>0:
# 				# iat.append(datetime.datetime.strptime(S2_get_stats.timestamps[idx],datetimeFormat)-datetime.datetime.strptime(S2_get_stats.timestamps[idx-1],datetimeFormat))
# 				# print datetime.datetime.strptime(S2_get_stats.timestamps[idx],datetimeFormat)-datetime.datetime.strptime(S2_get_stats.timestamps[idx-1],datetimeFormat)
# 				# time_delta.append(datetime.datetime.strptime(S2_get_stats.timestamps[idx],datetimeFormat)-datetime.datetime.strptime(S1_get_stats.timestamps[idx],datetimeFormat))
# 				# print datetime.datetime.strptime(S2_get_stats.timestamps[idx],datetimeFormat)-datetime.datetime.strptime(S1_get_stats.timestamps[idx],datetimeFormat)
# 		except IndexError:
# 			print 'null'

# # print iat













# with open('dummy') as f:
# 	for line in f:
# 		if "['tcp_csum:735b']" in line:
# 			print line
# 		else: continue





# with open("switch1-time.txt") as tf:
# 	for l in tf:
		
# 		l=l.split("\t")
# 		print l[3]
		# for i,v in enumerate(S2_get_stats.chksum2):
			# print v
			# print l[3]






# import S1_get_stats
# import S2_get_stats

# print len(S1_get_stats.chksum1)
# print len(S2_get_stats.chksum2)

# seen1=[]
# seen2=[]
# uniq_S1 = [x for x in S1_get_stats.chksum1 if x not in seen1 and not seen1.append(x)]   
# uniq_S2 = [x for x in S2_get_stats.chksum2 if x not in seen2 and not seen2.append(x)]   
# print len(seen1)



# print "Number of unique Checksum entries in S1",len(uniq_S1)
# print "Number of unique Checksum entries in S2",len(uniq_S2)

"""checking with DICTIONARY, does not help as key can't be duplicated, and i have Timestamps and Checksum duplicates"""
# c=[]
# time=[]
# dic=dict()
# i=0
# with open('switch1-result.txt', 'r') as tfile:
# 	for l in tfile:
# 		time.append(l[11:23])
# 		t=l[11:23] # Time
# 		# print len(l)
# 		c1=l.find('tcp_csum')
# 		c2=l.find(" ",c1)
# 		chksum=l[c1:c2]
# 		c.append(chksum)
# 		# print chksum
# 		dic[chksum]=t
# 		i+=1
# 		# if i==100: break
# print dic, len(dic)
# print len(time)
# print len(c)
# for k, v in dic.iteritems():
# 	if v=='tcp_csum:c0':
# 		print k


# a={1:"a", 2:"b"}
# b={1:"c",3:"b"}
# for k,v in a.iteritems():
# 	# print v
# 	if v is b[k]:
# 		print "yes" 


