import math

def is_primed(k):
    if k <= 1:
        print(False)
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(k)) + 1):
            if k % i == 0:
                is_prime = False
                break
    return is_prime
x, y = 2, 1000000  # define the range [x, y]

# create a boolean list to mark primes, assume all are prime initially
primes = [True] * (y + 1)

# 0 and 1 are not prime
primes[0], primes[1] = False, False

# Sieve of Eratosthenes to mark non-primes
for i in range(2, int(y ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, y + 1, i):
            primes[j] = False

# function to return the count of digit of n
def numberofDigits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt
    
# function to print the left shift numbers
def cal(num):
    fin_list = []
    digit = numberofDigits(num)
    powTen = pow(10, digit - 1)
    
    for i in range(digit - 1):
        
        firstDigit = num // powTen
        
        # formula to calculate left shift 
        # from previous number
        left = (num * 10 + firstDigit - 
               (firstDigit * powTen * 10))
        #print(left, end = " ")
        fin_list.append(left)
        # Update the original number
        num = left
    
    return fin_list

# collect primes in the range [x, y]
res = [i for i in range(x, y + 1) if primes[i]]
temp = []
primes_circ = 0
flag = True
for j in res:
    temp = cal(j)
    for k in temp:
        if not is_primed(k):
            flag = False
    if flag == True:
        primes_circ = primes_circ + 1
    flag = True

print(primes_circ)
