import pandas as pd
import numpy as np

# ──────────────────────────────────────────────────────────────
# Dataset: Titanic-like data generated with a fixed random seed
# (replace with pd.read_csv('titanic.csv') if you have the file)
# ──────────────────────────────────────────────────────────────
np.random.seed(42)
n = 891  # same size as the classic Titanic dataset

pclass = np.random.choice([1, 2, 3], n, p=[0.24, 0.21, 0.55])
sex    = np.random.choice(['male', 'female'], n, p=[0.65, 0.35])
age    = np.where(
    np.random.rand(n) < 0.20,          # ~20 % missing, like real data
    np.nan,
    np.random.normal(30, 14, n).clip(1, 80)
)
surv_prob = (pclass == 1) * 0.62 + (pclass == 2) * 0.47 + (pclass == 3) * 0.24
surv_prob += (sex == 'female') * 0.35
survived  = (np.random.rand(n) < surv_prob.clip(0, 1)).astype(int)

df = pd.DataFrame({'Survived': survived, 'Pclass': pclass, 'Sex': sex, 'Age': age})
df['SexCode'] = df['Sex'].map({'female': 0, 'male': 1})

print("=" * 60)
print("   MINI-PROJECT 5 — TITANIC DATASET ANALYSIS")
print("=" * 60)
print(f"Dataset shape : {df.shape}")
print(f"Missing Age   : {df['Age'].isna().sum()}")

# ── Task 1 ─────────────────────────────────────────────────────
# Group by Pclass → average Age and survival rate
print("\n── Task 1: Average Age & Survival Rate by Pclass ──")
task1 = df.groupby('Pclass').agg(
    Average_Age   = ('Age',      'mean'),
    Survival_Rate = ('Survived', 'mean')
).round(3)
print(task1.to_string())

# ── Task 2 ─────────────────────────────────────────────────────
# Normalize 'Age' with Min-Max, then Z-score (on non-null values)
print("\n── Task 2: Normalization of 'Age' ──")
age_min, age_max = df['Age'].min(), df['Age'].max()
age_mean, age_std = df['Age'].mean(), df['Age'].std()

df['Age_MinMax'] = (df['Age'] - age_min)  / (age_max - age_min)
df['Age_Zscore'] = (df['Age'] - age_mean) / age_std

print("  Formula: MinMax = (x - min) / (max - min)")
print("           Zscore = (x - mean) / std\n")
print(df[['Age', 'Age_MinMax', 'Age_Zscore']].dropna().head(8).round(4).to_string(index=False))

# ── Task 3 ─────────────────────────────────────────────────────
# Fill missing Age values with the column mean
print("\n── Task 3: Handle Missing Age Values ──")
missing_before = df['Age'].isna().sum()
df['Age'] = df['Age'].fillna(age_mean)
missing_after  = df['Age'].isna().sum()
print(f"  Missing before : {missing_before}")
print(f"  Fill value     : {age_mean:.2f}  (column mean)")
print(f"  Missing after  : {missing_after}")

# ── Task 4 ─────────────────────────────────────────────────────
# Group by SexCode → total number of survivors
print("\n── Task 4: Total Survivors by SexCode ──")
task4 = df.groupby('SexCode')['Survived'].sum()
task4.index = task4.index.map({0: 'Female (SexCode=0)', 1: 'Male (SexCode=1)'})
print(task4.to_string())

# ── Task 5 ─────────────────────────────────────────────────────
# New column: 'child' (Age < 18) or 'adult' (Age >= 18)
print("\n── Task 5: New Column 'AgeGroup' ──")
df['AgeGroup'] = np.where(df['Age'] < 18, 'child', 'adult')
print(df['AgeGroup'].value_counts().to_string())

# ── Task 6 ─────────────────────────────────────────────────────
# Pivot table: avg survival rate by Pclass (rows) × SexCode (cols)
print("\n── Task 6: Pivot Table — Avg Survival Rate (Pclass × SexCode) ──")
pivot = pd.pivot_table(
    df,
    values  = 'Survived',
    index   = 'Pclass',
    columns = 'SexCode',
    aggfunc = 'mean'
).round(3)
pivot.columns = ['Female (0)', 'Male (1)']
pivot.index.name = 'Pclass'
print(pivot.to_string())

print("\n" + "=" * 60)
print("   All 6 tasks completed successfully.")
print("=" * 60)