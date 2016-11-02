
i=0
with open("tcpdump-timedelay") as f:
	for line in f:
		line=line.split()
		l=line[0]
		# print l[0]
		if i<21895:
			print l, line[1]
		elif i>21895 and i<71384:
			st_l=float(l)+60
			print st_l, line[1]
		elif i>71384 and i<120870:
			st_l=float(l)+120
			print st_l, line[1]
		elif i>120870:
			st_l=float(l)+180
			print st_l, line[1]
		i=i+1