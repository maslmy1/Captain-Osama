from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Amadeus API credentials retrieved from environment variables
API_KEY = os.getenv("9dkLBmBAzGWYNet9VVw4I8d2uGMGbplY")
API_SECRET = os.getenv("ECPDmDQgAl6ieuB0")

# Step 1: Get the Access Token
def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    access_token = response.json()["access_token"]
    return access_token

# Step 2: Fetch Flight Offers
@app.route("/flight-offers", methods=["GET"])
def flight_offers():
    origin = request.args.get("origin")
    destination = request.args.get("destination")
    departure_date = request.args.get("departure_date")
    adults = request.args.get("adults", default=1, type=int)
    
    access_token = get_access_token()
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": departure_date,
        "adults": adults
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return jsonify(response.json())

# Start the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
