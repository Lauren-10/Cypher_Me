list1 = [1,5,2,3,4] #returns 3
list2 = [3,4,1,2,5] #returns 4
list3 = [1,2,3,4,5] #returns 0
list4 = [4,3,1,5,2] 
list5 = [5,4,3,2,1] #returns 10
list6 = [1,3,5,4,2]
list7 = [1,2,3,5,4] #returns 1
list8 = [3,5,4,2,1]


def num_inversions(test_list):
    maximum = max(test_list)
    minimum = min(test_list)
    size = len(test_list)
    sum_inversions = 0
    if(minimum == 1 and maximum - minimum == size - 1):
        for i in range(0, size):
            if (i - size) + test_list[i] > 0:
                sum_inversions = sum_inversions + (i - size) + test_list[i]
            else:
                continue
    else:
        for i in range(0, size):
            if(maximum - minimum) - (size - i) > 0:
                sum_inversions = sum_inversions + (maximum - minimum) - (size - i)
            else:
                continue
    return sum_inversions

#comparable quadratic algorithm
def inversionCount(arr):
    n = len(arr) 
    invCount = 0  

    for i in range(n - 1):
        for j in range(i + 1, n):
          
            # If the current element is greater than the next,
            # increment the count
            if arr[i] > arr[j]:
                invCount += 1
    return invCount  

"""
invertedsummax = 0
for i in range(1, len(listofinvertednums1)):
    invertedsummax = invertedsummax + i

#case where range of list is 1-anything
for i in range(0, len(listofinvertednums1)):
    if (len(listofinvertednums1) - 1 - i) - listofinvertednums1[i] > 0:
        invertedsum1 = invertedsum1 + (len(listofinvertednums1) - i) - listofinvertednums1[i] 
    else:
        continue

#case where range of list is min-max (truly any list)
for i in range(0, len(listofinvertednums2)):
    if ((listofinvertednums2[i] - minimum) - i)- len(listofinvertednums2)> 0:
        invertedsum2 = invertedsum2 + listofinvertednums2[i] - minimum 
    else:
        continue

print(invertedsummax - invertedsum1)
print(invertedsum2)
"""
print(num_inversions(list1))
print(inversionCount(list1))
print(num_inversions(list2))
print(num_inversions(list3))
print(num_inversions(list4))
print(num_inversions(list5))
print(num_inversions(list6))
print(num_inversions(list7))
print(num_inversions(list8))