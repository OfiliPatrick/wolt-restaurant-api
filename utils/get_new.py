from utils.get_restaurants import restaurants_data, open_restaurants, closed_restaurants
from geopy.distance import geodesic
import datetime

def get_new_restaurants(latitude, longitude):
    results = []
    sorted_open_restaurants = sorted(open_restaurants,key= lambda obj: datetime.datetime.strptime(obj['launch_date'], '%Y-%m-%d'), reverse = True)
    sorted_closed_restaurants = sorted(closed_restaurants,key= lambda obj: datetime.datetime.strptime(obj['launch_date'], '%Y-%m-%d'), reverse = True)
   
    for restaurant in sorted_open_restaurants:
        if len(results) == 10:
            break
        launch_date = restaurant["launch_date"].split("-")
        curr_date= datetime.date.today().strftime('%Y-%m-%d').split("-")
        end_date = datetime.datetime(int(curr_date[0]),int(curr_date[1]),int(curr_date[2]))
        start_date = datetime.datetime(int(launch_date[0]), int(launch_date[1]),int(launch_date[2]))
        num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        restaurant_long = restaurant["location"][0]
        restaurant_lat = restaurant["location"][1]
        input_param = (latitude, longitude)
        restaurant_param = (restaurant_lat, restaurant_long)
        distance = geodesic(input_param, restaurant_param).km

        if distance < 1.5 and num_months <= 4:
            results.append(restaurant)

    for restaurant in sorted_closed_restaurants:
        if len(results) == 10:
            break
        launch_date = restaurant["launch_date"].split("-")
        curr_date= datetime.date.today().strftime('%Y-%m-%d').split("-")
        end_date = datetime.datetime(int(curr_date[0]),int(curr_date[1]),int(curr_date[2]))
        start_date = datetime.datetime(int(launch_date[0]), int(launch_date[1]),int(launch_date[2]))
        num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        restaurant_long = restaurant["location"][0]
        restaurant_lat = restaurant["location"][1]
        input_param = (latitude, longitude)
        restaurant_param = (restaurant_lat, restaurant_long)
        distance = geodesic(input_param, restaurant_param).km

        if distance < 1.5 and num_months <= 4:
            results.append(restaurant)

    return results