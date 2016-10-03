with open('switch2-time.txt') as f:
	a="['"
	b="']"
	for l in f:
		# l=l.split('\t')
		l=l.strip()
		
		for char in a:
			l=l.replace(char,'')
			for char in b:
				l=l.replace(char,'')
		print l