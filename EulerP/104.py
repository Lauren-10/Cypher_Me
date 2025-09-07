s1 = 1
s2 = 1
sn = 0
yes = 0

for i in range(3, 1000000):
    sn = s1 + s2
    if len(str(sn)) < 18:
        continue
    elif 