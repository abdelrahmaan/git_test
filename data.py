import pandas as pd

df = pd.read_csv('training.csv', nrows= 20)
print(df.head())
print(df.sentiment.value_counts())