while True:
	try:
		a = input()
		b = input()
	except EOFError:
		break

	c = [0 for i in range(26)] #長度為26 裡面都是0
	d = [0 for i in range(26)] #長度為26 裡面都是0
	
	for i in a: #如a=abcdd 那abcdd都帶進i一次
		c[ord(i)-97] += 1
	for i in b:
		if(c[ord(i)-97]) > 0:
			c[ord(i)-97] -= 1
			d[ord(i)-97] += 1
	
	for i in range(26):
		for j in range(d[i]):
			print(chr(i+97), end="")
	print()