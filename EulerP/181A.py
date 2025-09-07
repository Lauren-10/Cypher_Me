#Python

#Pandigital fibbonaci beginnings and ends:
import sys
sys.set_int_max_str_digits(0)

def is_pandigital(int_list):
    if len(int_list) != 9:
        return False
    int_list.sort()
    for i in range(9):
        if int_list[i] != i+1:
            return False
    return True



i_1 = 1
i_2 = 1
i_next = 0
count = 2
digits = []
firsts = []
lasts = []
for i in range(329000,330000):
    i_next = i_1 + i_2
    i_1 = i_2
    i_2 = i_next
    count = count + 1
    if len(str(i_next)) > 575:
        digits = [int(digit) for digit in str(i_next)]
        firsts = [digits[i] for i in range(9)]
        lasts = [digits[len(digits) - (i + 1)] for i in range(9)]
        if is_pandigital(lasts) and is_pandigital(firsts):
            print(count)
            break
