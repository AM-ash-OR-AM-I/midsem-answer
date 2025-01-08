import math

# Helper function to calculate entropy
def entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

# Dataset summary: counts for each outcome given "Class: buys-computer"
total_count = 10
buy_yes = 6
buy_no = 4

# Overall entropy of the dataset
entropy_dataset = entropy([buy_yes / total_count, buy_no / total_count])

# Split by "Age"
age_counts = {
    "youth": {"yes": 1, "no": 3},
    "middle_aged": {"yes": 2, "no": 0},
    "senior": {"yes": 3, "no": 1},
}

# Split by "Student"
student_counts = {
    "yes": {"yes": 4, "no": 1},
    "no": {"yes": 2, "no": 3},
}

# Function to calculate information gain for an attribute
def information_gain(entropy_total, attribute_counts, total_samples):
    print(attribute_counts)
    weighted_entropy = 0
    for group, outcomes in attribute_counts.items():
        group_total = sum(outcomes.values())
        group_entropy = entropy([outcomes["yes"] / group_total, outcomes["no"] / group_total])
        weighted_entropy += (group_total / total_samples) * group_entropy
    return entropy_total - weighted_entropy

# Calculate information gain for "Age" and "Student"
info_gain_age = information_gain(entropy_dataset, age_counts, total_count)
info_gain_student = information_gain(entropy_dataset, student_counts, total_count)

print(entropy_dataset, info_gain_age, info_gain_student)