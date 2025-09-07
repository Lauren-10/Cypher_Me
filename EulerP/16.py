two = 1

for i in range(0,1000):
    two = two * 2

twos = [int(digit) for digit in str(two)]  

print(sum(twos))