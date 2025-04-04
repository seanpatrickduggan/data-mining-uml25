import matplotlib.pyplot as plt

def main():
    # Transactions
    transactions = [
        {'a', 'b', 'd', 'e'},
        {'b', 'c', 'd'},
        {'a', 'b', 'd', 'e'},
        {'a', 'c', 'd', 'e'},
        {'b', 'c', 'd', 'e'},
        {'b', 'd', 'e'},
        {'c', 'd'},
        {'a', 'b', 'c'},
        {'a', 'd', 'e'},
        {'b', 'd'}
    ]

    num_transactions = len(transactions)
    results = []

    for antecedent, consequent, rule_name in rules:
        # Count occurrences of the rule in the transactions
        both_present, x_present_y_absent, x_absent_y_present, both_absent = count_rule(antecedent, consequent, transactions)
        # Print the contingency "table"
        print("Rule:", rule_name)
        print(f"{antecedent} present and {consequent} present: {both_present}")
        print(f"{antecedent} present and {consequent} absent:  {x_present_y_absent}")
        print(f"{antecedent} absent and {consequent} present:  {x_absent_y_present}")
        print(f"{antecedent} absent and {consequent} absent:   {both_absent}\n")
        
        # Support 
        support = both_present / num_transactions
        # Confidence = P(X, Y) / P(X) = both_present / (number of transactions with X = both_present + x_present_y_absent)
        confidence = both_present / (both_present + x_present_y_absent)
        
        # P(Y) = Number of transactions with Y present / Total transactions
        prob_y = (both_present + x_absent_y_present) / num_transactions
        # Interest(X->Y) = (P(X, Y) / P(X)) * P(Y) = confidence * P(Y)
        interest = confidence * prob_y

        results.append({
            'rule': rule_name,
            'support': support,
            'confidence': confidence,
            'interest': interest
        })

    # Ranking the rules by each measure:
    print("Ranking by Support:")
    for rule in sorted(results, key=lambda x: x['support'], reverse=True):
        print(f"{rule['rule']}: Support = {rule['support']:.3f}")
    print()

    print("Ranking by Confidence:")
    for rule in sorted(results, key=lambda x: x['confidence'], reverse=True):
        print(f"{rule['rule']}: Confidence = {rule['confidence']:.3f}")
    print()

    print("Ranking by Interest:")
    for rule in sorted(results, key=lambda x: x['interest'], reverse=True):
        print(f"{rule['rule']}: Interest = {rule['interest']:.3f}")

    plot_rankings_matplotlib(results, 'support', 'Ranking by Support')
    plot_rankings_matplotlib(results, 'confidence', 'Ranking by Confidence')
    plot_rankings_matplotlib(results, 'interest', 'Ranking by Interest')


# Count occurance types for a rule
# X -> Y, X: antecedent, Y: consequent
def count_rule(X, Y, transactions):
    both_present = x_present_y_absent = x_absent_y_present = both_absent = 0
    for trans in transactions:
        x_in = X.issubset(trans)
        y_in = Y.issubset(trans)
        if x_in and y_in:
            both_present += 1
        elif x_in and not y_in:
            x_present_y_absent += 1
        elif not x_in and y_in:
            x_absent_y_present += 1
        else:
            both_absent += 1
    return both_present, x_present_y_absent, x_absent_y_present, both_absent

def plot_rankings_matplotlib(results, measure, title):
    sorted_results = sorted(results, key=lambda x: x[measure], reverse=True)

    rule_names = [rule['rule'] for rule in sorted_results]
    values = [rule[measure] for rule in sorted_results]
    
    plt.figure(figsize=(10, 6))
    plt.bar(rule_names, values)

    plt.title(title)
    plt.xlabel("Rule")
    plt.ylabel(measure)
    
    plt.grid(axis='y', linestyle='--')
    
    plt.ylim(0, 1)
    
    plt.tight_layout()
    
    filename = f"ranking_by_{measure}.png"
    plt.savefig(filename)

# List of rules
rules = [
    ({"b"}, {"c"}, "{b} -> {c}"),
    ({"a"}, {"d"}, "{a} -> {d}"),
    ({"b"}, {"d"}, "{b} -> {d}"),
    ({"e"}, {"c"}, "{e} -> {c}"),
    ({"c"}, {"a"}, "{c} -> {a}")
]

if __name__ == '__main__':
    main()
