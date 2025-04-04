import tabulate as tb

def main():
    # Main sequence
    main_seq = [{1, 2, 3}, {2, 4}, {2, 4, 5}, {3, 5}, {6}]
    
    # Standard test sequences
    test_sequences = [
        [{1}, {2}, {3}],
        [{1, 2, 3, 4}, {5, 6}],
        [{2, 4}, {2, 4}, {6}],
        [{1}, {2, 4}, {6}],
        [{1, 2}, {3, 4}, {5, 6}]
    ]

    # Timing constraints
    mingap = 0
    maxgap = 3
    maxspan = 5

    # Main sequence with nested sets
    nested_main_seq = [
        [{1, 2}, {3}],
        [{3, 4}, {5}],
        [{2, 4}, {6}],
        [{5, 6}, {7}],
        [{8}, {9}]
        ]

    # Test sequences with nested sets
    nested_test_sequences = [
        [[{1, 2}], [{3, 4}], [{6}]],
        [[{1}], [{5}], [{8}]],
        [[{1}], [{3}], [{10}]],
        [[{1}], [{5}], [{9}], [{8}]]
    ]

    main_results = []
    test_results = []

    # Main sequence test
    for i, sequence in enumerate(test_sequences):
        result = check_subsequence(main_seq, sequence, mingap, maxgap, maxspan)
        main_results.append((sequence, result))
    
    # Nested sequence test
    for i, sequence in enumerate(nested_test_sequences):
        result = check_subsequence(nested_main_seq, sequence, mingap, maxgap, maxspan)
        test_results.append((sequence, result))
        
    # Results
    print("Main Sequence:")
    print(main_seq)
    print("Main Sequence Results:")
    print(tb.tabulate(main_results, headers=["Subsequence", "Result"], tablefmt="grid"))
    print("Nested Main Sequence:")
    print(nested_main_seq)
    print("Nested Main Sequence Results:")
    print(tb.tabulate(test_results, headers=["Subsequence", "Result"], tablefmt="grid"))

def check_subsequence(main_seq, subsequence_candidate, mingap, maxgap, maxspan):
    def is_subset(subset, superset):
        # Both are sets
        if isinstance(subset, set) and isinstance(superset, set):
            return subset.issubset(superset)
            
        # Subset is a list of sets checking against a list of sets
        elif isinstance(subset, list) and isinstance(superset, list):
            # For each item in subset, check if it exists in superset
            for sub_item in subset:
                matched = False
                for super_item in superset:
                    if is_subset(sub_item, super_item):
                        matched = True
                        break
                if not matched:
                    return False
            return True
            
        # Single item versus list - check if item is in any element of list
        elif not isinstance(subset, (list, set)) and isinstance(superset, list):
            return any(subset in s for s in superset)
            
        # List versus single item - check if any list element matches single item
        elif isinstance(subset, list) and not isinstance(superset, (list, set)):
            return any(is_subset(s, superset) for s in subset)
            
        # Direct comparison for non-collection types
        else:
            return subset == superset

    def backtrack(candidate_idx, main_idx, times):
        # If we matched all elements in subsequence_candidate, check maxspan constraint
        if candidate_idx == len(subsequence_candidate):
            return times[-1] - times[0] <= maxspan
        
        # Try to match the current element of subsequence_candidate
        # with remaining elements in main_seq
        for i in range(main_idx, len(main_seq)):
            if is_subset(subsequence_candidate[candidate_idx], main_seq[i]):
                time = i + 1  # 1-indexed time
                
                # Check timing constraints with previous element
                if candidate_idx > 0:
                    prev_time = times[-1]
                    # Check mingap constraint
                    if time - prev_time <= mingap:  # interval must be > mingap
                        continue
                    # Check maxgap constraint
                    if time - prev_time > maxgap:
                        continue
                
                times.append(time)
                if backtrack(candidate_idx + 1, i + 1, times):
                    return True
                times.pop()
        
        return False
    
    return backtrack(0, 0, [])



if __name__ == "__main__":
    main()
