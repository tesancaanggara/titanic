#
# Titanic
# Tesanca Anggara
#

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/hermawansutrisno/Documents/tesanca's/S2/SEMESTER 1/data science/titanic 1.csv")

# Data Exploration
print(df.head(10))

# Columns and Data Types
df.info()
print (df.shape)

# Summary statistics for numerial columns
print(df.describe())

# Identify missing value
print(df.isnull().sum())

# Fill missing value 
df["Age"] = df["Age"].mean()
print(df.isnull().sum())