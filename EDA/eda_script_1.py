import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = '/content/lok_sabha_election_results_2024_expanded.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Display basic information about the DataFrame
print("Data Overview:")
print(df.head())
print("\nData Types:")
print(df.dtypes)

# Convert 'Total Votes' to numeric, coerce errors to NaN (if needed)
df['Total Votes'] = pd.to_numeric(df['Total Votes'], errors='coerce')

# Drop rows with NaN values in 'Total Votes' (if any)
df = df.dropna(subset=['Total Votes'])

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Visualization: Example of a bar plot for Total Votes by Constituency
plt.figure(figsize=(12, 8))
plt.bar(df['Constituency'], df['Total Votes'], color='skyblue')
plt.title('Total Votes by Constituency', fontsize=16)
plt.xlabel('Constituency', fontsize=14)
plt.ylabel('Total Votes', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Additional visualizations and analysis can be added as needed

