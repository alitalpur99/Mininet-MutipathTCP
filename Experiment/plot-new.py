import numpy
import matplotlib.pyplot as plt

cwnd=[]
time=[]
t=[]
i=0
fig = plt.figure()
ax1 = fig.add_subplot(111)

with open('cwnd_sf1_new') as f:
	a='['
	b=']'	
	
	#print line
	
	for line in f:
		line = line.rstrip()

		if i<1:
			offset = line[1:13]
		#line = line.split(' ')
		i+=1
		for char in a:
			line = line.replace(char,'')
			for char in b:
				line = line.replace(char,'')

		t.append(line[:12])
		cwnd.append(line[12:])		

for n in range(len(t)):
	
		time.append('{0:.8f}'.format(float(t[n])-float(offset)))
	
print max(cwnd)
print offset
print time
ax1.plot(time, cwnd, color = 'b', marker='*',  label = 'cwd')
ax1.grid(True)
# ax2.grid(True)
plt.xlabel('time')
plt.ylabel('CWD (number of packets)')
plt.legend(loc='upper right')
plt.title('CWND with kernel parameters, win=0 and recvbuff=0, RTT=40ms')
plt.show()


