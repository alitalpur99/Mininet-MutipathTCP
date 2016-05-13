# save in pox directory
# Simple plotting of 3 subplots to show flows, packets and bytes by reading from three separate files
# TO DO: plotting on web-based flow stats, per port, per switch, per traffic type

import matplotlib.pyplot as plt
import csv

x = []
y = []
z=[]
with open('flows.txt','r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
      x.append(int(row[0]))

plt.subplot(311)
plt.ylabel('flows/sec')
plt.title('Flow Statistics')
plt.plot(x, label='flows' )
#plt.show()
with open('packets.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
      y.append(int(row[0]))
plt.subplot(312)
plt.ylabel('packets/sec')
plt.plot(y, label='packets')        

#plt.show()
with open('bytes.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        z.append(int(row[0]))
plt.subplot(313)   
plt.xlabel('Time (interval 5 seconds)')
plt.ylabel('byets/sec')
plt.plot(z, label='bytes')

plt.show()
