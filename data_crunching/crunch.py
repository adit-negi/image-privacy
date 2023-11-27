import pandas as pd

# Load the CSV file
file_path = '/Users/aditnegi/Downloads/ImgPrivacyStudyResponses.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Assigning weights to responses (A-G)
weights = {'A': 1, 'B': 2, 'C': 3, 'D': 3, 'E': 2, 'F': 1, 'G': 0}
print(data.columns)
# Identifying scenario columns
# Replace with the actual names or indices of your scenario columns
scenario_columns = data.columns[10:]
print(scenario_columns)
# Initialize a dictionary to store total scores and count of responses for each scenario
total_scores = {col: 0 for col in scenario_columns}
count_responses = {col: 0 for col in scenario_columns}

# Calculate scores for each scenario
for col in scenario_columns:
    for response in data[col]:
        if response in weights:
            total_scores[col] += weights[response]
            count_responses[col] += 1

# Calculate average risk for each scenario
avg_risk_scores = {
    col: ((total_scores[col] / count_responses[col])/0.2) if count_responses[col] > 0 else 0
    for col in scenario_columns
}
print(avg_risk_scores)

avg_risk = {key: val for key, val in avg_risk_scores.items() }
# Output the average risk scores
print(len(avg_risk))
for scenario, avg_score in avg_risk.items():
    print(f'Average Risk for {scenario}: {avg_score}')
