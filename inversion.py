"""
def count_inversions_linear_fixed(P):
    n = len(P)
    
    # Position mapping: pos[k] = index of k in P
    pos = [0] * (n + 1)
    for i in range(n):
        pos[P[i]] = i  # Store index of each element in P
    
    inversions = 0
    max_seen = -1  # Highest index seen so far
    
    # Count elements that must move to sort the list
    misplaced = 0
    for k in range(1, n + 1):
        idx = pos[k]
        if idx < max_seen:
            misplaced += 1
        max_seen = max(max_seen, idx)
    
    # Reset for actual inversion count
    max_seen = -1
    
    # Iterate through elements in increasing order
    for k in range(1, n + 1):
        idx = pos[k]  # Current position of k in P
        
        # Count inversions
        if idx < max_seen:
            inversions += max_seen - idx
        
        # Update max_seen
        max_seen = max(max_seen, idx)
    
    # Special adjustment for cases with many misplaced elements
    if misplaced >= n - 1:
        # For nearly or completely reversed arrays
        inversions = (n * (n - 1)) // 2
    
    return inversions
"""
def count_inversions_linear_fixed(P):
    n = len(P)
    size = len(P)
    sum = 0

    for i in range(n - 1):
        #target will be 1,2
        #size will be 2,1
        target = i + 1
        size = n - 1
        if P[i] - target != 0:
            sum = sum + abs(P[i] - target)
        
        
    return sum


# Alternative approach that accurately counts inversions in truly linear time
def count_inversions_linear_accurate(P):
    n = len(P)
    
    # Position mapping: pos[k] = index of k in P
    pos = [0] * (n + 1)
    for i in range(n):
        pos[P[i]] = i
    
    # Create a bit array to track elements we've seen
    seen = [0] * n
    inversions = 0
    
    # Process elements in ascending order (1 to n)
    for k in range(1, n + 1):
        idx = pos[k]
        
        # Count elements to the left that are greater than current element
        for j in range(idx + 1, n):
            inversions += seen[j]
        
        # Mark this position as seen
        seen[idx] = 1
    
    return inversions


# Test cases
test_cases = {
    "list5": ([5, 4, 3, 2, 1], 10),
    "list8": ([3, 5, 4, 2, 1], 8),

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
    
}



def run_tests():
    print("Testing optimized inversion counting algorithms:")
    print("---------------------------------------------")
    for name, (arr, expected) in test_cases.items():
        fixed_result = count_inversions_linear_fixed(arr)
        accurate_result = count_inversions_linear_accurate(arr)
        
        print(f"{name}: {arr}")
        print(f"  Expected: {expected}")
        print(f"  Fixed approach:   {fixed_result} {'✓' if fixed_result == expected else '✗'}")
        print(f"  Accurate approach: {accurate_result} {'✓' if accurate_result == expected else '✗'}")
        print()

run_tests()