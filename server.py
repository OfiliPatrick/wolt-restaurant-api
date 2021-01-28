from flask import Flask, render_template, request, url_for,json
from utils.get_restaurants import restaurants_data, open_restaurants, closed_restaurants
from utils.get_popular import get_popular_restaurants
from utils.get_nearby import get_nearby_restaurants
from utils.get_new import get_new_restaurants

app = Flask(__name__) 
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/discovery')
def discovery():
    if not request.args.get("lat"):
        return render_template("error.html", parameter = "Latitude")

    elif not request.args.get("lon"):
        return render_template("error.html", parameter = "Longitude")

    else:
        latitude = request.args.get("lat")
        longitude = request.args.get("lon")
        popular_restaurants = get_popular_restaurants(latitude, longitude)
        new_restaurants = get_new_restaurants(latitude, longitude)
        nearby_restaurants = get_nearby_restaurants(latitude, longitude)

        response = {"sections": []}

        if popular_restaurants:
            response["sections"].append({"title" : "Popular Restaurants","restaurants": popular_restaurants})
         
        if new_restaurants:
            response["sections"].append({"title" : "New Restaurants","restaurants": new_restaurants})
        
        if nearby_restaurants:
            response["sections"].append({"title" : "Nearby Restaurants","restaurants": nearby_restaurants})
       
        return response
   

if __name__ == "__main__":
    app.run(debug=True)