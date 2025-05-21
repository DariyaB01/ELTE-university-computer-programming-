import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data
total_respondents = 120
importance_of_foreign_language = {'Positive': 79, 'Negative': 21}
willingness_to_increase_classes = {'Willing': 79, 'Unwilling': 21}
study_preferences = {'Multilingual groups': 58, 'Special subjects in foreign language': 30, 'Only the language': 12}
reasons_for_learning_language = {
    'Like to study languages and develop': 27,
    'Study in higher educational institutions': 22,
    'Career growth': 35,
    'Program requirement': 16
}

# Convert to numpy arrays for statistical analysis
importance_values = np.array(list(importance_of_foreign_language.values()))
willingness_values = np.array(list(willingness_to_increase_classes.values()))
study_preferences_values = np.array(list(study_preferences.values()))
reasons_values = np.array(list(reasons_for_learning_language.values()))

# Descriptive statistics
def print_descriptive_stats(data, title):
    print(f"{title} - Descriptive Statistics")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Median: {np.median(data):.2f}")
    print(f"Standard Deviation: {np.std(data):.2f}")
    print(f"Variance: {np.var(data):.2f}")
    print()

# Inferential statistics (Chi-square test for independence)
def chi_square_test(observed, title):
    chi2, p = stats.chi2_contingency([observed, total_respondents - observed])[:2]
    print(f"{title} - Chi-square Test")
    print(f"Chi-square statistic: {chi2:.2f}")
    print(f"P-value: {p:.4f}")
    if p < 0.05:
        print("Result: Significant (reject the null hypothesis)")
    else:
        print("Result: Not significant (fail to reject the null hypothesis)")
    print()

print_descriptive_stats(importance_values, "Importance of Learning a Foreign Language")
print_descriptive_stats(willingness_values, "Willingness to Increase Practical Classes")
print_descriptive_stats(study_preferences_values, "Study Preferences")
print_descriptive_stats(reasons_values, "Reasons for Learning a Foreign Language")

chi_square_test(importance_values, "Importance of Learning a Foreign Language")
chi_square_test(willingness_values, "Willingness to Increase Practical Classes")
chi_square_test(study_preferences_values, "Study Preferences")
chi_square_test(reasons_values, "Reasons for Learning a Foreign Language")

# Plot 1: Pie Chart for importance of learning a foreign language
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.pie(importance_of_foreign_language.values(), labels=importance_of_foreign_language.keys(), autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightcoral'])
plt.title('Importance of Learning a Foreign Language')

# Plot 2: Bar Chart for willingness to increase practical classes
plt.subplot(2, 2, 2)
plt.bar(willingness_to_increase_classes.keys(), willingness_to_increase_classes.values(), color=['green', 'red'])
plt.title('Willingness to Increase Practical Classes')
plt.ylabel('Percentage')
plt.ylim(0, 100)

# Plot 3: Bar Chart for study preferences
plt.subplot(2, 2, 3)
plt.bar(study_preferences.keys(), study_preferences.values(), color=['blue', 'orange', 'purple'])
plt.title('Study Preferences')
plt.ylabel('Percentage')
plt.ylim(0, 100)
plt.xticks(rotation=45)

# Plot 4: Pie Chart for reasons for learning a foreign language
plt.subplot(2, 2, 4)
plt.pie(reasons_for_learning_language.values(), labels=reasons_for_learning_language.keys(), autopct='%1.1f%%', startangle=140, colors=['gold', 'lightgreen', 'lightpink', 'lightgray'])
plt.title('Reasons for Learning a Foreign Language')

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# Context from the article
context = """
The article discusses the problems and prospects of the formation and development of multilingual education in Kazakhstan.
Key highlights include:
- A survey conducted among students of Pavlodar Pedagogical University showed that many of them (79%) answered positively about the importance of learning a foreign language for their future specialty.
- Despite the positive attitude, 21% of the students do not want to increase the number of practical classes in a foreign language.
- Study preferences show that 58% prefer studying in multilingual groups, while 30% prefer special subjects in a foreign language, and 12% think only the language itself matters.
- The reasons for learning a foreign language are diverse: 27% like to study languages and want to develop, 22% need it for studying in higher educational institutions, 35% for career growth, and 16% study because the program requires it.

Challenges identified include:
- Non-compliance of current qualification requirements with those of a multilingual specialist.
- Lack of normative and program-methodical support for multilingual education.
- Insufficient knowledge of foreign experiences in implementing multilingual education.
- Need for developing a unified concept of training multilingual specialists.
"""

print(context)
