import numpy as np
import pandas as pd

classifiers = ["Decision Tree", "Naive Bayes", "SVM"]

raw_data = [
        ["Anneal",        898, 92.09, 79.62, 87.19],
        ["Australia",     690, 85.51, 76.81, 84.78],
        ["Auto",          205, 81.95, 58.05, 70.73],
        ["Breast",        699, 95.14, 95.99, 96.42],
        ["Cleve",         303, 76.24, 83.50, 84.49],
        ["Credit",        690, 85.80, 77.54, 85.07],
        ["Diabetes",      768, 72.40, 75.91, 76.82],
        ["German",       1000, 70.90, 74.70, 74.40],
        ["Glass",         214, 67.29, 48.59, 59.81],
        ["Heart",         270, 80.00, 84.07, 83.70],
        ["Hepatitis",     155, 81.94, 83.23, 87.10],
        ["Horse",         368, 85.33, 78.80, 82.61],
        ["Ionosphere",    351, 89.17, 82.34, 88.89],
        ["Iris",          150, 94.67, 95.33, 96.00],
        ["Labor",          57, 78.95, 94.74, 92.98],
        ["Led7",         3200, 73.34, 73.16, 73.56],
        ["Lymphography",  148, 77.03, 83.11, 86.49],
        ["Pima",          768, 74.35, 76.04, 76.95],
        ["Sonar",         208, 78.85, 69.71, 76.92],
        ["Tic-tac-toe",   958, 83.72, 70.04, 98.33],
        ["Vehicle",       846, 71.04, 45.04, 74.94],
        ["Wine",          178, 94.38, 96.63, 98.88],
        ["Zoo",           101, 93.07, 93.07, 96.04]
    ]

def compute_z_statistic(acc_a, acc_b, sample_size):
    p = (acc_a + acc_b) / 2
    se = np.sqrt((2 * p * (1 - p)) / sample_size)
    return (acc_a - acc_b) / se

def compare_classifiers(data):
    classifiers = ["Decision Tree", "Naive Bayes", "SVM"]
    pairs = [("Decision Tree", "Naive Bayes"), ("Decision Tree", "SVM"), ("Naive Bayes", "SVM")]
    results = {c1: {c2: [0, 0, 0] for c2 in classifiers} for c1 in classifiers}

    for _, row in data.iterrows():
        n = row["Size"]
        for c1, c2 in pairs:
            z = compute_z_statistic(row[c1] / 100, row[c2] / 100, n)
            if z > 1.96:
                results[c1][c2][0] += 1 # c1 wins
                results[c2][c1][1] += 1 # c2 loses
            elif z < -1.96:
                results[c1][c2][1] += 1 # c1 loses
                results[c2][c1][0] += 1 # c2 wins
            else:
                results[c1][c2][2] += 1 # draw
                results[c2][c1][2] += 1 # draw

    return results



def show_win_loss_draw(results):
    classifiers = ["Decision Tree", "Naive Bayes", "SVM"]
    num_datasets = sum(results[classifiers[0]][classifiers[1]])

    matrix = []
    for row_clf in classifiers:
        row_data = []
        for col_clf in classifiers:
            if row_clf == col_clf:
                row_data.append(f"0-0-{num_datasets}")
            else:
                w, l, d = results[row_clf][col_clf]
                row_data.append(f"{w}-{l}-{d}")
        matrix.append(row_data)

    df = pd.DataFrame(matrix, index=classifiers, columns=classifiers)
    print("\nWin-Loss-Draw Table:")
    print(df)

if __name__ == "__main__":
    data = pd.DataFrame(raw_data, columns=["Data Set", "Size", "Decision Tree", "Naive Bayes", "SVM"])
    results_summary = compare_classifiers(data)
    show_win_loss_draw(results_summary)