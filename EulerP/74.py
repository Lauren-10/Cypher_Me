f = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}
chain_cache = {1:1, 2:1, 145:1, 40585:1, 169:3, 363601:3, 1454:3, 871:2, 45361:2, 872:2, 45362:2}
sdf = lambda n: sum(f[d] for d in str(n))

def find_chain_length(n):
    try:
        return chain_cache[n]
    except:
        chain_length = find_chain_length(sdf(n)) + 1
        chain_cache[n] = chain_length
        return chain_length

N = 1000000
L = 60
for _ in range(1):
    q = [*filter(lambda n: find_chain_length(n) == L, range(N + 1))] or [-1]
    print(len(q))	