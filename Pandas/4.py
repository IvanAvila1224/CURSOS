import pandas as pd

reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)
print(reviews)
