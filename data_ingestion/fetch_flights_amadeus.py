import requests

# Amadeus credentials
API_KEY = "9dkLBmBAzGWYNet9VVw4I8d2uGMGbplY"
API_SECRET = "ECPDmDQgAl6ieuB0"

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
    print("Access token obtained.")
    return access_token

# Step 2: Fetch Flight Offers
def fetch_flight_offers(access_token, origin, destination, departure_date, adults=1):
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
    print("Flight data fetched successfully.")
    return response.json()

if __name__ == "__main__":
    # Define search parameters
    origin = "JFK"  # Origin airport code
    destination = "LAX"  # Destination airport code
    departure_date = "2024-12-20"  # Departure date (YYYY-MM-DD)
    
    # Authenticate and fetch data
    token = get_access_token()
    flight_data = fetch_flight_offers(token, origin, destination, departure_date)
    
    # Print flight data
    print(flight_data)

