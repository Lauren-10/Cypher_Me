def count_inversions_linear_adjusted(P):
    n = len(P)
    
    #Dynamic Programming!!!
    # Position mapping: pos[k] = index of k in P
    pos = [0] * (n + 1)
    for i in range(n):
        pos[P[i]] = i  # Store index of each element in P

    
    inversions = 0
    max_seen = 0  # Highest index seen so far
    num_times_max_changed = 0 #keeps track of the numnber of times max changes

    misplaced_count = 0  # Number of elements that must move to sort the list

    # Iterate through elements in increasing order
    for k in range(0, n + 1):
        idx = pos[k]  # Current position of k in P
        
        # Count how many elements appeared after their correct position
        if idx < max_seen:
            inversions += max_seen - idx
            misplaced_count += 1  # Track misplaced elements

        # Update max_seen
        if (idx > max_seen):
            num_times_max_changed += 1
        max_seen = max(max_seen, idx)



    # Adjust for elements needing movement
    
    inversions -= max(0, misplaced_count - 1)
    
    #for i in range(0,(n-1)):
    #edge case
    if(misplaced_count == n-1):
        print()

    return inversions

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
    "len4_f": ([3, 4, 2, 1], 6),
    "len4_g": ([4, 3, 1, 2], 5),
    
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
    "len6_f": ([1, 2, 5, 6, 3, 4], 4),
    
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

# Run tests
results = {name: (count_inversions_linear_adjusted(lst), expected) for name, (lst, expected) in test_cases.items()}
print(results)
