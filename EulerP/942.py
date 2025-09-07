N = 74207281
MOD = 10**9+7

r = pow(2, N+1, MOD) - 2
for i in range(N):
    r -= pow(2, i**2 % N, MOD)
print(r % MOD)