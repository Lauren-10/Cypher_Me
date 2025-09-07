from math import isqrt
from functools import lru_cache

#populate a list of squares all less than 10^12 as well as their original number
squares = [] 
for i in range(1000000):
    squares.append(i**2)

 
def is_s_number(n, return_witness=False, allow_single_zero=True):
    if n < 0:
        return (False, None) if return_witness else False
    
    r = isqrt(n)
    if r * r != n:
        return (False, None) if return_witness else False
    
    s = str(n)
    target = r
    L = len(s)

    @lru_cache(maxsize=None)
    def dfs(i, acc):
        if acc > target:
            return None  # prune
        if i == L:
            return [] if acc == target else None
        
        # extend next chunk from s[i:j]
        best = None
        for j in range(i+1, L+1):
            chunk = s[i:j]
            # Disallow leading zeros like "05"
            if chunk[0] == '0' and not (allow_single_zero and len(chunk) == 1):
                break  # any longer chunk will also start with '0'
            val = int(chunk)
            res = dfs(j, acc + val)
            if res is not None:
                return [chunk] + res  # return first found witness
        return None

    witness = dfs(0, 0)
    ok = witness is not None
    return (ok, witness) if return_witness else ok

#check and see if the squares can be represented as a sum of the digits of the original number.
digits = []
for j in range(len(squares)):
    if is_s_number(squares[j], False, True):
        digits.append(j)

print(sum(digits))


