import math

def s(n, d):
    int_r = int(sqrt(n))
    snd = []
    n_sq = n * 10**(d*2)
    n_sqrt = int_r*10**(d)
    for i in range(1, d+1):
        FLAG = True
        for j in range(1, 10):
            if n_sq < (n_sqrt + j*10**(d-i))**2:
                n_sqrt += (j-1)*10**(d-i)
                snd.append(j-1)
                FLAG = False
                break
        if FLAG:
            n_sqrt += 9*10**(d-i)
            snd.append(9)
    return sum(snd)

print(s(13,1000))