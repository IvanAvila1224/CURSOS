import pandas as pd
#----1
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

reviews_descrption = reviews['description']
print(reviews_descrption)

