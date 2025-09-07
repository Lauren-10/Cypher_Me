import math


def split_number_half(number):
    num_str = str(number)
    length = len(num_str)
    
    # Calculate the midpoint for splitting
    midpoint = length // 2 
    
    # Split the string into two halves
    first_half_str = num_str[:midpoint]
    second_half_str = num_str[midpoint:]
    
    # Convert back to integers if needed
    first_half_int = int(first_half_str) if first_half_str else 0
    second_half_int = int(second_half_str) if second_half_str else 0
    
    return first_half_int, second_half_int

square = 0
a = 0
b = 0
summ = 0
for i in range(10000000): #num squares below 10^17
    square = i**2
    a,b = split_number_half(square)
    if int(str(a) + str(b)) == square:
        summ = summ + int(square)

print(summ)


