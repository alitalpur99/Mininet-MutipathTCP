# Print Congestion Window graph from TCP Probe output file
import numpy
import matplotlib.pyplot as plt
from matplotlib import style
# style.use('fivethirtyeight') # for style guide

col=list()
cwd=list()
ssthresh=list()
time=list()


fig = plt.figure()
ax1 = fig.add_subplot(111)
# ax2 =fig.add_subplot(211)
i=0
t=[]
srtt=[]
time_diff=[]
c=[]



# open the TCP_probe output file
with open('/home/ali/tcp-minint.out', 'r') as infile:
    
	for line in infile:
		# line = line.rstrip()
		fields = line.split() #if (line.split()[1] or line.split()[2]) == '5001']
		
		# print fields
        # print len(fields)

        # TIME DIFF PRINT OUT
		# t.append(line.split()[0])
		# print t
		# if i > 0:
		# 	time_diff.append(float('{0:.8}'.format(float(t[i])-float(t[i-1])))*1000) # time diff in millisec
		# i+=1
			
		if fields[2].split(':')[1] == '5201':
			# print line

			time.append(line.split()[0])# col 0 is for time values
			c.append(int(line.split()[6]))	# col 6 is for cong window values
			cwd.append((int(fields[6]))* 1460 / 1024.0) # convert cwd in KB
			# cwd.append(line.split()[6]) # COL NUMBER 7
			# srtt.append(line.split()[-1])
			
			ssthresh.append((int(fields[7]))* 1500 / 1024.0) # col 7 is for slow start threshold values

        # APPEND ONLY SENDER/CLIENT SIDE CONGESTION WINDOW, SSTHRESH , TIME VALUES
		# if fields[1].split(':')[1]!='5001': #port other than 5001 is sender's port
		# 	cwd.append(line.split()[6])	# col 6 is for cong window values
		# 	time.append(line.split()[0])# col 0 is for time values
			# if fields[7] >= '2147483647': 
			# 	ssthresh.append('0')
   #      	else:
		# if i>1000:
		# 	break
# OUPUT OF TIME_DIFF SAVE TO A FILE
# with open('time_diff','a') as f:
# 	f.write(str(time_diff))
# with open('time','a') as f:
# 	f.write(str(time))
	

# print type(cwd), type(ssthresh)
# print len(cwd), len (ssthresh), len(time) 



z= numpy.array(cwd,dtype=int)*1 # to get max value and convert to int value
# y= numpy.array(ssthresh,dtype=int)*1460
# print 'time diff in millisec \n', time_diff
# print time
print 'cwnd in kB \n', cwd, '\n maximum value =', max(z)
print '\n===================\n'
# print 'cwnd  \n', c, '\n total values =', len(c), '\n maximum value =', max(c)
print '\n===================\n'

# print '\nslow start thresh \n', ssthresh
# print '\n===================\n'
# print '\ntime \n', time
# print srtt


# ax1.plot(time,z, color = 'b',marker='*',  label = 'cwd')
# ax1.plot(time,y,  color = 'r',marker='*',  label = 'ssthresh')

ax1.plot(time, cwd, color = 'b', marker='*',  label = 'cwd')
# ax1.plot( time, ssthresh,  color = 'r', marker='.',  label = 'ssthresh')

ax1.grid(True)
# ax2.grid(True)
plt.xlabel('time')
plt.ylabel('CWD (in kB)')
plt.legend(loc='upper right')
plt.title('CWND - TCP RENO 2h-2s,BW=100Mbps,RTT=80ms,loss=0,Queue=default')

plt.show()






#=============================================================================================================

''' Initial tries'''

#========================================================================================================
# from collections import defaultdict

# from csv import reader
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use('fivethirtyeight')
# #ls -l | awk '{print $7}' check columns

# # cwd = defaultdict(list)
# cwd=[]
# ssth = []
# col =[]
# i = 0
# time = []

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# # with open('/home/ali/tcpout','r') as f:
# # 	data = list(reader(f, delimiter =' '))
# # 	print data[6]


# def second(lst):
#     return map(lambda e: e[1], lst)

# with open('/home/ali/tcpout-cubic', 'r') as infile:
    
#         # CHANGE IT SO IT TAKES THE SOURCE PORT OTHER THAN 5001
#     # i = len(infile.readlines())
#     # print 'Number of lines in file are ',i
#     for line in infile:

#         # if i > 15:
#         fields = line.split()#strip().split(' ')
#         print fields
#         # print len(fields)
        
#         if fields[1].split(':')[1] == '5001':# or fields[7] == '2147483647':
#             pass
#         else:

#             time.append(fields[0])
#             c = int(fields[6]) # COL NUMBER 7
#             # sport = fields[1].split(':')[1]
#             # print c
#             # cwd.append(line.split()[6])
#             cwd.append(c )#* (1480 / 1024.0))


#             col.append(line.split()[7])
#             print fields[7]
#             # if fields[7] == '2147483647':
#             #     continue
#             # else:   
#             #     ssth.append(fields[7]) 

#         # insert i variable to limit the number of samples shown
#         # i+=1
#         # if i > 500:
#         # 	break
       
# for i in range(len(col)):
# 	if col[i] == '2147483647':
# 		continue #ssth.append(0)
# 	else:	
# 		ssth.append(col[i])
# # print col
# # val = cwd.values()
# # print time#, cwd, ssth
# # print ssth, time, cwd
# print len(cwd), len(ssth), len(time)
# # print ssth

# ax1.plot(time, cwd, color = 'b',  label = 'cwd')
# ax1.plot(time, ssth, color = 'r',marker='+',  label = 'ssthresh')
# plt.xlabel('time')
# plt.ylabel('CWD & ssthres')
# plt.legend(loc='upper right')
# plt.title('Cubic Congestion Window graph')

# # plt.show()


#+===================================================================================================================================

# from csv import reader
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use('fivethirtyeight')
# #ls -l | awk '{print $7}' check columns

# cwd = []
# ssth = []
# col =[]
# i = 0

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# # with open('/home/ali/tcpout','r') as f:
# # 	data = list(reader(f, delimiter =' '))
# # 	print data[6]

# with open('/home/ali/tcpout-cubic', 'r') as infile:
#     for line in infile:
#     	# CHANGE IT SO IT TAKES THE SOURCE PORT OTHER THAN 5001
    	
#         cwd.append(line.split()[6])
#         col.append(line.split()[7])

#         # insert i variable to limit the number of samples shown
#         # i+=1
#         # if i > 500:
#         # 	break
       
# for i in range(len(col)):
# 	if col[i] == '2147483647':
# 		ssth.append(0)
# 	else:	
# 		ssth.append(col[i])
# # print col
# # print cwd
# # print ssth

# ax1.plot(cwd, color = 'b',marker='*',  label = 'cwd')
# ax1.plot(ssth, color = 'r',marker='*',  label = 'ssthresh')
# plt.xlabel('time')
# plt.ylabel('CWD & ssthres')
# plt.legend(loc='upper right')
# plt.title('Cubic Congestion Window graph')

# plt.show()


