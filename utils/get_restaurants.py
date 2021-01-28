from flask import json

with open('./static/data/restaurants.json', 'r') as jsonfile:
    restaurants_data = json.loads(jsonfile.read())

open_restaurants = []
closed_restaurants = []

for restaurant in restaurants_data["restaurants"]:
    if restaurant["online"]:
        open_restaurants.append(restaurant)
    else:
        closed_restaurants.append(restaurant)