K = int(input())
M, C, S = 10**9+7, range(81*K+1), [0,1,4,9,16,25,36,49,64,81]
d = lambda n: n>1 and (n==89 or d(sum(S[int(c)] for c in str(n))))

p = [i in S for i in C]
for _ in range(K-1):
    p = [sum(p[j-s] for s in S if j>=s) % M for j in C]

print(sum(v for i,v in enumerate(p) if i and d(i)) % M)	