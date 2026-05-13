import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

print("=" * 50)
print("        TITANIC DATASET ANALYSIS")
print("=" * 50)

# 1. Total number of passengers
total = len(df)
print(f"\n1. Total Passengers        : {total}")

# 2. Number of survived passengers
survived = df['Survived'].sum()
print(f"2. Survived Passengers     : {survived}")

# 3. Number of not survived passengers
not_survived = total - survived
print(f"3. Not Survived Passengers : {not_survived}")

# 4. Average age
avg_age = df['Age'].mean()
print(f"4. Average Age             : {avg_age:.2f}")

# 5. Average fare
avg_fare = df['Fare'].mean()
print(f"5. Average Fare            : {avg_fare:.2f}")

# 6. Number of male passengers
males = df[df['Sex'] == 'male'].shape[0]
print(f"6. Male Passengers         : {males}")

# 7. Number of female passengers
females = df[df['Sex'] == 'female'].shape[0]
print(f"7. Female Passengers       : {females}")

# 8. Maximum age
max_age = df['Age'].max()
print(f"8. Maximum Age             : {max_age}")

# 9. Minimum age
min_age = df['Age'].min()
print(f"9. Minimum Age             : {min_age}")

# 10. Survival rate (percentage)
survival_rate = (survived / total) * 100
print(f"10. Survival Rate          : {survival_rate:.2f}%")

# 11. Average age of survived passengers
avg_age_survived = df[df['Survived'] == 1]['Age'].mean()
print(f"11. Avg Age of Survived    : {avg_age_survived:.2f}")

print("\n" + "=" * 50)