import pandas as pd

wine_reviews = pd.read_csv("wine.csv")
print(wine_reviews)
print(wine_reviews.shape)
print(wine_reviews.shape[0])
print(wine_reviews.shape[1])
print ('\n\t head \n')
print(wine_reviews.head)