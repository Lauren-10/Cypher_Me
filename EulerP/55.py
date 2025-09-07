def p55(C = 10000):
	res = 0
	for n in range(1, C):
		term = n
		term_rev = int(str(term)[::-1])
		for k in range(50):
			term += term_rev
			term_rev = int(str(term)[::-1])
			if term_rev == term:
				break
		else:  # loop fell through
			res += 1
	return res

p56 = lambda C=100: max(sum(map(int, str(x**y))) for x in range(C) for y in range(C))

def p57(C = 1000):
	a, b = 3, 2
	res = 0
	for n in range(2, C+1):
		a, b = a + 2*b, a + b
		if len(str(a)) > len(str(b)):
			res += 1
	return res


print(p55())
print(p56())
print(p57())