from utils.get_restaurants import restaurants_data, open_restaurants, closed_restaurants
from geopy.distance import geodesic

def get_popular_restaurants(latitude, longitude):
    results = []
    sorted_open_restaurants = sorted(open_restaurants, key = lambda obj: obj["popularity"], reverse = True)
    sorted_closed_restaurants = sorted(closed_restaurants, key = lambda obj: obj["popularity"], reverse = True)
    
    for restaurant in sorted_open_restaurants:
        if len(results) == 10:
            break
        restaurant_long = restaurant["location"][0]
        restaurant_lat = restaurant["location"][1]
        input_param = (latitude, longitude)
        restaurant_param = (restaurant_lat, restaurant_long)
        distance = geodesic(input_param, restaurant_param).km
        if distance < 1.5:
            results.append(restaurant)

    for restaurant in sorted_closed_restaurants:
        if len(results) == 10:
            break
        restaurant_long = restaurant["location"][0]
        restaurant_lat = restaurant["location"][1]
        input_param = (latitude, longitude)
        restaurant_param = (restaurant_lat, restaurant_long)
        distance = geodesic(restaurant_param, input_param).km
        if int(distance) < 1.5:
            results.append(restaturant)

    return results