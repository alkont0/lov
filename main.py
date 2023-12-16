from flask import Flask, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36")

@app.route('/get_location')
def get_location():
    location = geolocator.geocode("Hyderabad")

    if location:
        response = {
            "latitude": location.latitude,
            "longitude": location.longitude
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Location not found"}), 404
