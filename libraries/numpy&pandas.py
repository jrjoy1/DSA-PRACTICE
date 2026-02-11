import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/student-mat.csv", sep=";")
df['school'] = df['school'].str.strip().str.lower()

age_array = df['age'].values

# Compute age statistics
age_mean = np.mean(age_array)
age_median = np.median(age_array)
age_std = np.std(age_array)
age_min = np.min(age_array)
age_max = np.max(age_array)

# Add as new columns
df['age_mean'] = age_mean
df['age_median'] = age_median
df['age_std'] = age_std
df['age_min'] = age_min
df['age_max'] = age_max

print(df.head())

# Distribution of age
plt.hist(df['age'], bins=10, color='orange', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.show()