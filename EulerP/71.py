ceildiv = lambda a, b: -(-a // b)

A, D = map(int, input().split())

n = [0] * D
for d in range(1, D):
    n[d]+= ceildiv(d, A) - ceildiv(d, A+1) - 1
    n[2*d::d] = [k-n[d] for k in n[2*d::d]]
print(sum(n))	