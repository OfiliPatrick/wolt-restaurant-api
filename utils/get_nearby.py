from utils.get_restaurants import restaurants_data, open_restaurants, closed_restaurants
from geopy.distance import geodesic
import datetime

def get_nearby_restaurants(latitude, longitude):
    results = []
    sorted_open_restaurants = sorted(open_restaurants, key = lambda obj: geodesic((latitude, longitude), (obj["location"][1], obj["location"][0] )).km)
    sorted_closed_restaurants = sorted(closed_restaurants, key = lambda obj: geodesic((latitude, longitude), (obj["location"][1], obj["location"][0] )).km)
        
    for restaurant in sorted_open_restaurants:
        if len(results) == 10:
            break
        restaurant_long = restaurant["location"][0]
        restaurant_lat = restaurant["location"][1]
        input_param = (latitude, longitude)
        restaurant_param = (restaurant_lat, restaurant_long)
        distance = geodesic(input_param, restaurant_param).km
        if distance < 1.5:
            results.append((restaurant, distance))

    for restaurant in sorted_open_restaurants:
        if len(results) == 10:
            break
        restaurant_long = restaurant["location"][0]
        restaurant_lat = restaurant["location"][1]
        input_param = (latitude, longitude)
        restaurant_param = (restaurant_lat, restaurant_long)
        distance = geodesic(input_param, restaurant_param).km
        if distance < 1.5:
            results.append((restaurant, distance))

    return results
