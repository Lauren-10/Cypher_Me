def memodict(f):
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

@memodict
def trinumdiv(n):
    numbers = range(1,n+1)
    total = sum(numbers)
    return len([j for j in range(1,total+1) if total % j == 0])

def main():
    nums = range(100000)
    for n in nums:
        if trinumdiv(n) > 500:
           print(n)
           break

main()