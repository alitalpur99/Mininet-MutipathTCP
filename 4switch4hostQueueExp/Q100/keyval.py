# """
# using dictionaries, take key as Chksum and Time as value (since dict keys can't be duplicated) 
# """

# """ For S1 """
# time1=[]
# t1=[]
# c1=[]
# chksum1=[]
# dic1=dict()
# with open("switch1-time.txt") as f1:
# 	for l1 in f1:
# 		l1=l1.strip()
# 		l1=l1.split("\t")
# 		t1.append(l1[0])
# 		c1.append(l1[3])
# 		# print l[3]
# 		time1=l1[0]
# 		chksum1=l1[3]
# 		dic1[chksum1]=time1

# # print dic1, len(dic1)

# # ########################################################################################################################


# """ For S2 """

# time2=[]
# chksum2=[]
# t2=[]
# c2=[]
# dic2=dict()
# with open("switch4-time.txt") as f2:
# 	for l2 in f2:
# 		l2=l2.strip()
# 		l2=l2.split("\t")
# 		t2.append(l2[0])
# 		c2.append(l2[3])
# 		# print l[3]
# 		time2=l2[0]
# 		chksum2=l2[3]
# 		dic2[chksum2]=time2
# # # print dic2, len(dic2)

# # # print t1,len(t1)
# # #####################################################
# # '''COMPARING TWO DICTIONARIES'''
# dic=dict()
# open("s1s4keyok","w").close()
# with open("s1s4keyok","w+") as fkey:
# 	for k,v in dic1.items():
# 		for key,val in dic2.items():
# 			if k==key:
# 			# print "s1", k,v, "--", "S2", key,val
# 				fkey.write(str(k)+" "+ str(v)+" "+str(key)+" "+str(val))
# 				fkey.write("\n")

# # #########################################################
# # """ sorting dictionaries using Time values """

# import operator
# sorted_dic1 = sorted(dic1.items(), key=operator.itemgetter(1))
# # print sorted_dic1, len(sorted_dic1)
# sorted_dic2 = sorted(dic2.items(), key=operator.itemgetter(1))

# # """print sorted dic1 and 2"""
# open("sorteddic1","w").close()
# with open("sorteddic1","w+") as ff:
# 	for i in range(len(sorted_dic1)):
# 		ff.write(str(sorted_dic1[i])+" "+ "\n")

# open("sorteddic2","w").close()
# with open("sorteddic2","w+") as ff:
# 	for i in range(len(sorted_dic2)):
# 		ff.write(str(sorted_dic2[i])+" "+ "\n")


# # ###########################################
# # """Print time of the S1"""
# # dic1_t= [x[1] for x in sorted_dic1]
# # # for i in range(len(dic1_t)):
# # # 	print dic1_t[i].split(":")[2]
# # """Print time of the S2"""
# # dic2_t= [x[1] for x in sorted_dic2]
# # # for i in range(len(dic2_t)):
# # # 	print dic2_t[i].split(":")[2]

# # # """ Get the time tuple as dic_t or chksum tuple as dic_v"""

# dic2_t = [x[1] for x in sorted_dic2] # take teh time
# dic2_v = [x[0] for x in sorted_dic2] # take the value / chksum
# # # print dic2_v


# open("sortedtupless1s4","w").close()

# with open("sortedtupless1s4","w+") as sf:

# 	with open("sorteddic1") as df:

# 		for line in df:
# 			line=line.strip()
# 			for i in range(len(sorted_dic2)):
# 				if dic2_v[i] in line:
# 					sf.write(str(dic2_v[i]) + " " +str(dic2_t[i])+" " +str(line))
# 					sf.write("\n")
# # 			# else:
# 			# 	print "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
# 	# print dic2_t[i].split(":")[2]
# 	# print dic2_t[i]


import datetime
from datetime import timedelta

times1=[]
times2=[]
t_s1=[]
diff=[]
with open("sortedtupless1s4") as f:
	
	datetimeFormat = '%H:%M:%S.%f' 
	for l in f:
		l=l.strip()
		l=l.split()
		times2.append(l[1])
		times1.append(l[3])

	# print times1
	for n in range(len(times1)):
		s=str(times1[n])
		a="'"
		b="')"
		for char in a:
			s=s.replace(char,"")
			for char in b:
				s=s.replace(char,"")
			t_s1.append(s)
		diff.append(datetime.datetime.strptime(times2[n],datetimeFormat)-datetime.datetime.strptime(t_s1[n],datetimeFormat))
		# print datetime.datetime.strptime(times2[n],datetimeFormat)-datetime.datetime.strptime(t_s1[n],datetimeFormat)
	# print t_s1
open("owd","w").close()
with open("owd","w+") as f:
	for i in range(len(diff)):
		t2_s=str(t_s1[i])
		t2_time=float(t2_s.split(":")[2])

		diff_s=str(diff[i])
		diff_sec=diff_s.split(":")[2]

		# print t2_time

		if float(t2_time)<20:

			t2_time=t2_time+60
			print t2_time
			f.write(str(t2_time)+" "+str(diff_sec))
			f.write("\n")	
		else:
			f.write(str(t2_time)+" "+str(diff_sec))
			f.write("\n")



# print diff


# s="'13:15:27.404')"
# a="'"
# b=")"
# for char in a:
# 	s=s.replace(char," ")
# 	print s
# 	for char in b:
# 		s=s.replace(char," ")
# print s


'''checking for same key val in both dic, NOT WORKING'''
# same=set(dic1.items()) & set(dic2.items())
# print same, len(same)