# print the timestamps for the packet-ins at Switch s1/s2

field=[]
l=[]

'''to empty the file contents'''

open('/home/ali/pox-results/s1-result.txt', 'w').close()

with open('/home/ali/pox-results/s1-file') as f:

	i=0
	for line in f:
		line = line.rstrip()
		# print 'full line****************',line
		i+=1
		words = line.split(' ')
		if line.startswith('2016'):# and i<=500:
			field.append(words[1:3])
		
for n in range(len(field)):
	if 'OFPT_PACKET_IN' in field[n]:
		l.append(field[n])
with open('/home/ali/pox-results/s1-result.txt', 'a') as wfile:
	for item in l:
		wfile.write("%s\n" % item)	
		time = item[0].split(',')
		print time

# filter(lambda l: 'OFPT_PACKET_IN' in l, field)
# print field


###Code for S2 switch

'''to empty the file contents'''
# open('/home/ali/s2-time.txt', 'w').close()

# with open('/home/ali/s2-file') as f:
# 	# print f.read()
# 	'''to limit the ouput lines to 200'''
# 	x=0
# 	for line in f:
		
# 		line = line.rstrip()
# 		# print 'full line****************',line
# 		x+=1
# 		words = line.split(' ')
		
# 		if line.startswith('2016') and words[2] == 'OFPT_PACKET_IN': 
# 			# print words[1:3]
# 			with open('/home/ali/s2-time.txt', 'a') as wfile:
# 				wfile.write(words[1])
# 				wfile.write('\t ')
# 				wfile.write(words[2])
# 				wfile.write('\n')

# 		if x==500: break
