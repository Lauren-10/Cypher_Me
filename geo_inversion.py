"""
def criss_cross_inversion_counting(arr):
    inverted_sum = 0
    criss = []
    cross = []
    cross_it = 0
    size = len(arr)
    target = 0
    num_to_compare = 0
    #counts of crisses
    for i in range(size):
        target = i + 1
        if arr[i] >= target:
            criss.append([arr[i], arr[i] - target])
    
    for i in range(size):
        if arr[i] >= target:
            cross_it = cross_it + 1
        else:
            cross.append([arr[i], abs(arr[i] - target), cross_it])
            cross_it = cross_it - arr[i] - target

    #pass through to count the crisses 
    for i in range(0, len(criss)):
        inverted_sum = inverted_sum + criss[i][1]
    
    #pass through to count the crosses
    for i in range(0, len(cross)):
        if(cross[i][2] > cross[i][1]):
            inverted_sum = inverted_sum + (cross[i][1] - cross[i][2])

    return inverted_sum
"""
def criss_cross_inversion_counting(arr):
    maximum = max(arr)
    minimum = min(arr)
    size = len(arr)
    inversion_sum = 0
    misplaced_count = 0
    maximum_swaps = (size * (size-1))/2
    #criss iteration
    for i in range(size):
        if arr[i] != minimum:
            inversion_sum = inversion_sum + (maximum - arr[i]) + i
        else:
            minimum += 1
    #cross iteration
    
    for i in range(1, size + 1):
        if arr[size - i] < (maximum - i + 1):
            inversion_sum = inversion_sum - abs(arr[size - i] - (maximum - i))
            misplaced_count = misplaced_count + 1
    
    if(inversion_sum != maximum_swaps or inversion_sum != 0):
        inversion_sum = inversion_sum - misplaced_count
    
    return inversion_sum

#test cases
# Test cases
test_cases = {
    # Length 1
    "len1_a": ([1], 0),
    
    # Length 2
    "len2_a": ([1, 2], 0),
    "len2_b": ([2, 1], 1),
    
    # Length 3
    "len3_a": ([1, 2, 3], 0),
    "len3_b": ([1, 3, 2], 1),
    "len3_c": ([2, 1, 3], 1),
    "len3_d": ([2, 3, 1], 2),
    "len3_e": ([3, 1, 2], 2),
    "len3_f": ([3, 2, 1], 3),
    
    # Length 4
    "len4_a": ([1, 2, 3, 4], 0),
    "len4_b": ([4, 3, 2, 1], 6),
    "len4_c": ([2, 1, 4, 3], 2),
    "len4_d": ([3, 1, 4, 2], 3),
    "len4_e": ([1, 4, 2, 3], 2),
    
    # Length 5
    "len5_a": ([1, 2, 3, 4, 5], 0),
    "len5_b": ([5, 4, 3, 2, 1], 10),
    "len5_c": ([2, 4, 1, 5, 3], 4),
    "len5_d": ([3, 5, 2, 1, 4], 6),
    "len5_e": ([1, 5, 3, 2, 4], 3),
    
    # Length 6
    "len6_a": ([1, 2, 3, 4, 5, 6], 0),
    "len6_b": ([6, 5, 4, 3, 2, 1], 15),
    "len6_c": ([3, 1, 6, 2, 5, 4], 7),
    "len6_d": ([4, 2, 5, 1, 6, 3], 8),
    "len6_e": ([2, 5, 1, 6, 3, 4], 5),
    
    # Length 7
    "len7_a": ([1, 2, 3, 4, 5, 6, 7], 0),
    "len7_b": ([7, 6, 5, 4, 3, 2, 1], 21),
    "len7_c": ([4, 2, 6, 1, 7, 3, 5], 10),
    "len7_d": ([3, 7, 2, 5, 1, 6, 4], 11),
    "len7_e": ([5, 2, 7, 4, 1, 6, 3], 12),
    
    # Length 8
    "len8_a": ([1, 2, 3, 4, 5, 6, 7, 8], 0),
    "len8_b": ([8, 7, 6, 5, 4, 3, 2, 1], 28),
    "len8_c": ([4, 8, 2, 6, 3, 7, 1, 5], 14),
    "len8_d": ([5, 2, 7, 4, 8, 1, 6, 3], 15),
    "len8_e": ([3, 8, 5, 1, 7, 2, 6, 4], 15),
    
    # Length 9
    "len9_a": ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
    "len9_b": ([9, 8, 7, 6, 5, 4, 3, 2, 1], 36),
    "len9_c": ([5, 9, 2, 7, 4, 1, 8, 3, 6], 19),
    "len9_d": ([4, 8, 3, 7, 1, 9, 5, 2, 6], 17),
    "len9_e": ([6, 3, 9, 5, 2, 8, 1, 7, 4], 22),
    
    # Length 10
    "len10_a": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
    "len10_b": ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 45),
    "len10_c": ([5, 10, 3, 8, 2, 7, 1, 9, 4, 6], 24),
    "len10_d": ([7, 3, 10, 5, 8, 2, 9, 1, 6, 4], 27),
    "len10_e": ([4, 9, 6, 1, 8, 3, 10, 2, 7, 5], 22)
}


def run_tests():
    print("Testing optimized inversion counting algorithms:")
    print("---------------------------------------------")
    for name, (arr, expected) in test_cases.items():
        fixed_result = criss_cross_inversion_counting(arr)
        
        
        print(f"{name}: {arr}")
        print(f"  Expected: {expected}")
        print(f"  Fixed approach:   {fixed_result} {'Passed' if fixed_result == expected else 'Failed'}")
        print()
    


run_tests()    
    
            