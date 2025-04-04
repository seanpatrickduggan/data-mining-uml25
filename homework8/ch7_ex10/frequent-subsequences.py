import itertools

def main():
    min_support = 0.5
    max_candidate_length = 4
    sequence_database = [
        [{"A", "B"}, {"C"}, {"D", "E"}, {"C"}], #S1
        [{"A", "B"}, {"C", "D"}, {"E"}],        #S2
        [{"B"}, {"A"}, {"B"}, {"D", "E"}],      #S3
        [{"C"}, {"D", "E"}, {"C"}, {"E"}],      #S4
        [{"B"}, {"A"}, {"B", "C"}, {"A", "D"}]  #S5
    ]

    all_occurring = []
    frequent = []

    # Loop through all possible candidates (length 1 to max_candidate_length)
    for candidate_length in range(1, max_candidate_length + 1):
        # Generate all possible candidates of the current length
        # using itertools.product to create combinations of letters A-E
        for candidate in itertools.product("ABCDE", repeat=candidate_length):
            # Check if the candidate is a subsequence of any sequence in the database
            occurances = sum(is_subsequence(candidate, seq) for seq in sequence_database)
            # Calculate support
            num_sequences = len(sequence_database)
            support = occurances / num_sequences
            if support >= min_support:
                frequent.append((candidate, support))
            else:
                all_occurring.append((candidate, support))

    # A prettier string for the candidate
    def candidate_str(candidate):
        return "<{" + "} {".join(candidate) + "}>"

    print("All Occurring Subsequences:")
    for candidate, support in all_occurring:
        print(f"Subsequence: {candidate_str(candidate)}")
        print(f"Support: {support:.3f}")

    print("------------------------------")

    print("Frequent Subsequences (Support ≥ 50%):")
    for candidate, support in frequent:
        print(f"Subsequence: {candidate_str(candidate)}")
        print(f"Support: {support:.3f}")

# Check if a candidate is a subsequence of a sequence
def is_subsequence(candidate, sequence):
    i = 0
    for itemset in sequence:
        if candidate[i] in itemset:
            i += 1
            if i == len(candidate):
                return True
    return False


if __name__ == '__main__':
    main()
