import math

def isprime(num):

    if num <= 1:
        return False 
    if num == 2:
        return True   
    if num % 2 == 0:
        return False  
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False 
    return True 

def p51():
	patterns = ['{0}{1}{3}{3}{3}{2}', '{0}{3}{1}{3}{3}{2}',
				'{0}{3}{3}{1}{3}{2}', '{0}{3}{3}{3}{1}{2}',
				'{3}{0}{1}{3}{3}{2}', '{3}{0}{3}{1}{3}{2}',
				'{3}{0}{3}{3}{1}{2}', '{3}{3}{0}{1}{3}{2}',
				'{3}{3}{0}{3}{1}{2}', '{3}{3}{3}{0}{1}{2}']
	res = 10 ** 6  # Just in case there were multiple families (there aren't)
	for pattern in patterns:
		for A in range(10):
			if pattern[1] == '0' and A == 0:
				continue
			for B in range(10):
				for C in [1, 3, 7, 9]:
					tmin = 1 if pattern[1] == '3' else 0
					non_primes = tmin
					pmin = int(pattern.format(A, B, C, tmin))
					for t in range(tmin, 10):
						p = int(pattern.format(A, B, C, t))
						if not isprime(p):
							non_primes += 1
							if non_primes > 2:
								break
					if non_primes == 2:
						res = min(res, pmin)
	return res

print(p51())