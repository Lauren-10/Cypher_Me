import numpy as np

A = np.array([
 [6,1,5,1,2,3,5,5,5,3],
 [2,5,4,5,1,4,1,5,1,1],
 [4,2,1,3,5,5,1,0,1,0],
 [4,5,4,5,1,4,1,5,1,1],
 [6,1,5,1,2,3,5,5,5,1],
 [0,2,2,2,6,1,6,2,0,4]
], dtype=int)

def show(mask, title):
    print(title)
    for r in mask:
        print(''.join('#' if x else '.' for x in r))
    print()

# 1) single residue (try r=5 and r=1)
for r in range(7):
    show(A==r, f"value == {r}")


summ = 0
for i in range(6):
    summ = summ + sum(A[i])
print(summ)

mask = np.isin(A, [4,5,6])  # True where value is 5 or 6

def show(part):
    return "\n".join("".join("#" if v else "." for v in row) for row in part)

# show the whole mask
print(show(mask))