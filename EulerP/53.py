def p53():
	binom = 1144066
	k = 10
	res = 0
	for n in range(23, 101):
		while binom * k // (n-k+1) > 10**6:
			binom = binom * k // (n-k+1)
			k -= 1
		res += n - 2*k + 1
		binom = binom * (n+1) // (n-k+1)
	return res

print(p53())
