import pandas as pd
df = pd.read_csv('Disease and symptoms dataset.csv')
print('Shape:', df.shape)
print('Unique diseases:', df['diseases'].nunique())
print(df['diseases'].value_counts()[:5])
