import requests
import sys

def get_weather(city, api_key):
    base_url = "http://api.weatherstack.com/current"
    weather_url = f"{base_url}?access_key={api_key}&query={city}"

    try:
        # Send en forespørsel til API og hent svaret
        response = requests.get(weather_url)
        response.raise_for_status()  # Sjekker for HTTP-feil
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
            print(f"\nFant ikke byen '{city}'. Vennligst prøv igjen.")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP-feil: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Feil med forespørselen: {req_err}")
    except Exception as e:
        print(f"En uventet feil oppstod: {e}")

def main():
    if len(sys.argv) != 2:
        print("Bruk: python weather_stack.py <by>")
        sys.exit(1)  # Avslutt programmet med feilkode

    city = sys.argv[1]
    api_key = "din_weatherstack_api_nøkkel"  # Bytt ut med din API-nøkkel
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
