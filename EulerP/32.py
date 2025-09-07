products = set()
is_pandigital = lambda n, length=9: len(n)==length and not '1234567890'[:length].strip(n)
N = int(input())
for i in range(2, 99):
    j = i+1
    while i*j < 8976:
        if is_pandigital(f"{i}{j}{i*j}", N): products.add(i*j)
        j+= 1
print (sum(products))