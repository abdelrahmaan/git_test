import pandas as pd

df = pd.read_csv('training.csv', nrows= 20)
print(df.head(10))
print(df.sentiment.value_counts())
