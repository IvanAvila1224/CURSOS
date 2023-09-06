import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews)
print('\n sub-dataset \n select top 1 * from winesmag\n')
reviews_iloc_n = reviews.iloc[100]
print(reviews_iloc_n)

print('\n sub-dataset \n select top 1 * from winesmag\n')
reviews_iloc_n = reviews.iloc[:,0]
print(reviews_iloc_n)

print('\n sub-dataset \n select top 3 country from winesmag\n')
reviews_country_top3 = reviews.iloc[:3,0]
print(reviews_country_top3)

print('\n sub-dataset row 2,3 \n select country from winesmag\n')
reviews_country_r2_r3 = reviews.iloc[1:3,0]
print(reviews_country_r2_r3)

print('\n sub-dataset row 1,2,3 \n select country from winesmag\n')
reviews_country_r1_r2_r3 = reviews.iloc[1:3,0]
print(reviews_country_r1_r2_r3)

print('\n sub-dataset row 1,2,3 \n select country from winesmag\n')
reviews_country_descrip_r1_r2_r3 = reviews.iloc [[0,1,2], [0,1] ]
print(reviews_country_descrip_r1_r2_r3)

print('\n sub-dataset row -5 \n select country from winesmag\n')
reviews_country_5 = reviews.iloc [-5: ]
print(reviews_country_5)

print('\n sub-dataset row country \n select country from winesmag\n')
reviews_country = reviews.loc [:, ['taster_name', 'taster_twitter_handle', 'points']]
print(reviews_country)

print('\n sub-dataset title \n select country from winesmag\n')
reviews_country_title = reviews.set_index("title")
print(reviews_country_title)

print('\n sub-dataset selection wine is italian or not \n select country from winesmag\n')
reviews_italy = reviews.country == 'Italy'
print(reviews_italy)

print('\n sub-dataset selection wine is italian or not \n select country from winesmag\n')
reviews_descrption = reviews['description']
print(reviews_descrption)


