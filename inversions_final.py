def count_inversions_linear_adjusted(P):
    n = len(P)
    
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
    "list1": ([1, 5, 2, 3, 4], 3),
    "list2": ([3, 4, 1, 2, 5], 4),
    "list3": ([1, 2, 3, 4, 5], 0),
    "list4": ([4, 3, 1, 5, 2], 6),
    "list5": ([5, 4, 3, 2, 1], 10),
    "list6": ([1, 3, 5, 4, 2], 4),
    "list7": ([1, 2, 3, 5, 4], 1),
    "list8": ([3, 5, 4, 2, 1], 8),
    "list9": ([3, 1, 5, 4, 2], 5)
}

# Run tests
results = {name: (count_inversions_linear_adjusted(lst), expected) for name, (lst, expected) in test_cases.items()}
print(results)
