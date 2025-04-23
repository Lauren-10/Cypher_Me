def right_left_sum_inversion(arr):
    size = len(arr)
    inversion_count = 0
    right_sum = 0
    left_sum = 0
    total_sum = 0
    cumulative_arr = []
    for i in range(size):
        cumulative_arr.append((i+1) - arr[i])
        total_sum = total_sum + (i+1 - arr[i])

    if(total_sum != 0):
        return -1
    
    for i in range(size):
        right_sum = right_sum - arr[i]
        left_sum = left_sum + arr[i]
        if(right_sum > i+1):
            inversion_count = 
    print(cumulative_arr)


print(right_left_sum_inversion([3,5,1,4,2]))