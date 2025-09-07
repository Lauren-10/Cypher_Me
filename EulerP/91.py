import math
N = int(input())
t = sum(min(x*m//y, m*(N - y)//x)
        for x in range(1, N+1)
        for y in range(1, N)
        for m in [math.gcd(x, y)])
print(2*t + 3*N*N)