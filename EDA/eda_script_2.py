!pip install pandas matplotlib seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data into a DataFrame
df = pd.read_csv('election_insights.csv')

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(df.head())

# Basic statistics of the dataset
print("\nBasic statistics of the dataset:")
print(df.describe(include='all'))

# Count of insights by party
party_counts = df['Party Details'].value_counts()
print("\nCount of insights by party:")
print(party_counts)

# Bar plot of the count of insights by party
plt.figure(figsize=(12, 7))
sns.barplot(x=party_counts.index, y=party_counts.values, palette='viridis')
plt.xlabel('Party', fontsize=12)
plt.ylabel('Count of Insights', fontsize=12)
plt.title('Count of Insights by Party', fontsize=16)
plt.xticks(rotation=45)
plt.show()

# Insights by State
state_counts = df['State'].value_counts()
print("\nCount of insights by state:")
print(state_counts)

# Bar plot of the count of insights by state
plt.figure(figsize=(12, 7))
sns.barplot(x=state_counts.index, y=state_counts.values, palette='viridis')
plt.xlabel('State', fontsize=12)
plt.ylabel('Count of Insights', fontsize=12)
plt.title('Count of Insights by State', fontsize=16)
plt.xticks(rotation=45)
plt.show()

# Detailed analysis of seat distribution
# Handle NaNs and non-string values
df['Seats Won'] = df['Seats Won'].fillna('').astype(str)
df['Seats Won'] = df['Seats Won'].str.split(', ').apply(lambda x: [i for i in x if i.isdigit()])
df = df.explode('Seats Won').reset_index(drop=True)
df['Seats Won'] = pd.to_numeric(df['Seats Won'], errors='coerce').dropna().astype(int)

print("\nDetailed statistics on seats won:")
print(df['Seats Won'].describe())

# Histogram of seats won
plt.figure(figsize=(12, 7))
sns.histplot(df['Seats Won'], bins=10, kde=True, color='skyblue')
plt.xlabel('Seats Won', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Seats Won', fontsize=16)
plt.show()

# Select only numeric columns for correlation analysis
numeric_cols = df.select_dtypes(include=['number'])

# Correlation analysis
plt.figure(figsize=(10, 6))
correlation_matrix = numeric_cols.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix', fontsize=16)
plt.show()

# Pairplot to visualize relationships between different features
plt.figure(figsize=(12, 7))
sns.pairplot(df, hue='Party Details', palette='viridis', diag_kind='kde')
plt.show()

# Boxplot for detailed distribution of seats won by party
plt.figure(figsize=(12, 7))
sns.boxplot(x='Party Details', y='Seats Won', data=df, palette='viridis')
plt.xlabel('Party', fontsize=12)
plt.ylabel('Seats Won', fontsize=12)
plt.title('Distribution of Seats Won by Party', fontsize=16)
plt.xticks(rotation=45)
plt.show()

