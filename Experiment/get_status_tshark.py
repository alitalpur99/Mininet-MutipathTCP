i=0
count=0
fields=[]
with open('/home/ali/pox-results/00exp/h1.txt','r') as f:
	for line in f:
		i=i+1
		line=line.split()
		# print line
			
		if line[2]=='10.0.0.1':# and :
			line=line[5:]
			# print line
			if line[4]=='55000' or line[6]=='55000'  or line[8]=='55000' or line[9]=='55000':
				print line
		 		count = count+1
		# if i==100: break
# 			if line[6]=='55000':
print count
