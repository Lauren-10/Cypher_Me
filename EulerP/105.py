import math
from itertools import combinations

def special(q):
    mx = 0
    for i in range(2,len(q)):
        t = set()
        for c in combinations(q,i):
            s = sum(c)
            if s in t or s<=mx: return False
            t.add(s)
        mx=max(t)
    return True

sets = []
sets_cleaned = []
summation = 0 

with open("EulerP/sets.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        sets.append(line.rstrip().split(','))

for i in sets:
    sets_cleaned.append(list(map(int, i)))

for i in sets_cleaned:
    if special(i) == True:
        summation = summation + sum(i)

print(summation)



