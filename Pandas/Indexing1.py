import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews)
print('\nselect country from winesmag\n')
print(reviews.country)
print('\nselect country from winesmag\n')
reviews_country = reviews['country']
print(reviews_country)

print('\nselect top 1 country from winesag\n')
reviews_country_top1 = reviews['country'][2]
print(reviews_country_top1)
