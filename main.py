# num_bath, num_bed, num_guests, num_bedrooms, city, state_province
import pandas as pd
import matplotlib
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pylab
import matplotlib.pyplot as plt



print("Welcome to our AirBnB price predictor!")

city = input("What city is your AirBnB located? ")
state = input("What state or province is your AirBnB located? ")
country = input("What country is your AirBnB located? ")
num_bedrooms = input("How many bedrooms does your AirBnb have? ")
num_bed = input("How many beds does your AirBnb have? ")
num_bath = input("How many bathrooms does your AirBnb have? ")
num_guests = input("How many guests does your AirBnb house? ")

new_airbnb = pd.DataFrame({
	'bathrooms' : [num_bath], 
	'beds' : [num_bed],	
	'guests' : [num_guests], 
	'bedrooms' : [num_bedrooms],
	'city' : [city], 
	'state': [state], 
	'country' : [country]
})

print(f"Your AirBnB is in {new_airbnb["city"][0]}, {new_airbnb["state"][0]}, {new_airbnb["country"][0]} with the following amenitites:")
print(f"Number of beds: {new_airbnb["beds"][0]}")
print(f"Number of bedrooms: {new_airbnb["bedrooms"][0]}")
print(f"Maximum number of guests: {new_airbnb["guests"][0]}")
print(f"Number of bathrooms: {new_airbnb["bathrooms"][0]}")

df_raw = pd.read_csv('airbnb.csv')
df = df_raw[['address', 'price', 'bathrooms', 'beds', 'guests', 'bedrooms']]

for index, row in df.iterrows():
	commas = 0
	for char in row['address']:
		if char == ',':
			commas += 1
	if commas != 2:
		df = df.drop(index)

df[['city', 'state', 'country']] = df['address'].str.split(", ",expand=True)
df = df.drop(['address'], axis=1)
df = df.dropna(subset=['price'])

#### df now has the address split into it's city, state, country components
