def p45():
	Pm = Hn = 40755
	m, n = 165, 143
	while True:
		if Pm < Hn:
			m += 1
			Pm = m * (3*m - 1) // 2
		else:
			n += 1
			Hn = n * (2*n - 1)
		if Pm == Hn:
			return Pm

print(p45())