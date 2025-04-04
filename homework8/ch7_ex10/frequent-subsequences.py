import itertools

def is_subsequence(candidate, sequence):
    i = 0
    for itemset in sequence:
        if candidate[i] in itemset:
            i += 1
            if i == len(candidate):
                return True
    return False

def main():
    min_support_count = 3
    max_candidate_length = 4
    sequence_database = [
        [{"A", "B"}, {"C"}, {"D", "E"}, {"C"}],
        [{"A", "B"}, {"C", "D"}, {"E"}],
        [{"B"}, {"A"}, {"B"}, {"D", "E"}],
        [{"C"}, {"D", "E"}, {"C"}, {"E"}],
        [{"B"}, {"A"}, {"B", "C"}, {"A", "D"}]
    ]
    all_occurring = []
    frequent = []

    for candidate_length in range(1, max_candidate_length + 1):
        for candidate in itertools.product("ABCDE", repeat=candidate_length):
            support = sum(is_subsequence(candidate, seq)
                          for seq in sequence_database)
            if support:
                all_occurring.append((candidate, support))
            if support >= min_support_count:
                frequent.append((candidate, support))

    def candidate_str(candidate):
        return "<{" + "} {".join(candidate) + "}>"

    print("All Occurring Subsequences (Support > 0):\n")
    for candidate, count in all_occurring:
        print(f"Subsequence: {candidate_str(candidate)}")
        print(f"Support: {count / len(sequence_database):.3f}")

    print("Frequent Subsequences (Support ≥ 50%):\n")
    for candidate, count in frequent:
        print(f"Subsequence: {candidate_str(candidate)}")
        print(f"Support: {count / len(sequence_database):.3f}")

if __name__ == '__main__':
    main()
