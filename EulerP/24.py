from itertools import permutations
# Find the one millionth permutation of '0123456789'
print (''.join(list(permutations('0123456789',10))[999999]))