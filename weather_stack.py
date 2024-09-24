import requests
import sys

def get_weather(city, api_key):
    base_url = "http://api.weatherstack.com/current"
    weather_url = f"{base_url}?access_key={api_key}&query={city}"

    # Send en forespørsel til API og hent svaret
    response = requests.get(weather_url)
    data = response.json()

    # Hvis byen finnes
    if "current" in data:
        current = data["current"]

        # Vis værdata
        print(f"\nVæret i {city.capitalize()}:")
        print(f"Temperatur: {current['temperature']}°C")
        print(f"Fuktighet: {current['humidity']}%")
        print(f"Beskrivelse: {current['weather_descriptions'][0]}")
    else:
        print(f"\nFant ikke byen {city}. Vennligst prøv igjen.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bruk: python weather_stack.py <by>")
    else:
        city = sys.argv[1]
        api_key = "din_weatherstack_api_nøkkel"  # Bytt ut med din API-nøkkel
        get_weather(city, api_key)
