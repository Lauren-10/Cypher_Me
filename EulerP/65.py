import sys
sys.set_int_max_str_digits(0)  # Remove the 4300 digit limit

nx, ny = 1, 2
for i in range(2, int(input())+1):
    m = 2*i//3 if i%3==0 else 1
    nx, ny = ny, nx + ny*m

print(sum(map(int, str(ny))))