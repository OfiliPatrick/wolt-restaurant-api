# Wolt-restaurant-api

## Description

Flask API able to retrieve the following Restaurant data:

- “Popular Restaurants”: highest popularity value first (descending order)
- “New Restaurants”: Newest launch_date first (descending). This list has also a special rule: launch_date must be no older than 4 months.
- “Nearby Restaurants”: Closest to the given location first (ascending).

## API Usage

1. Enter a "lat"(latitude) and "lon"(longitude) parameter at the "/discovery" endpoint.
2. Make a GET Request.
3. JSON Response is returned displaying relevant information.

## Live Demo

Find the live version of the API here: [wolt-restaurant-api](https://wolt-restaurant-api.herokuapp.com/)