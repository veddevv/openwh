import requests  # Importerer requests for å gjøre API-forespørsler

# Funksjon som henter vær basert på en by
def get_weather(city="Oslo"):  # "Oslo" er standard by hvis ingen annen er spesifisert
    # Dictionary som inneholder byer med deres breddegrad og lengdegrad
    coordinates = {
        'Oslo': (59.91, 10.75),
        'Bergen': (60.39, 5.32),
        'Trondheim': (63.43, 10.39),
        'Stavanger': (58.97, 5.73),
        'Tromsø': (69.65, 18.96),
        'Kristiansand': (58.15, 8.00),
        'Drammen': (59.74, 10.20),
        'Ålesund': (62.47, 6.15),
        'Bodø': (67.28, 14.40),
        'Tønsberg': (59.27, 10.41),
        'Arendal': (58.46, 8.77)  # Arendal lagt til med riktige koordinater
    }

    # Sjekker om byen finnes i listen over koordinater
    if city in coordinates:
        latitude, longitude = coordinates[city]  # Henter bredde- og lengdegrad for byen
        # Bygger URL for API-forespørselen til Open-Meteo basert på koordinatene
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)  # Sender forespørsel til API-et
        data = response.json()  # Konverterer svaret til JSON-format
        return data['current_weather']  # Returnerer dagens værdata
    else:
        return "Byen er ikke tilgjengelig i databasen"  # Feilmelding hvis byen ikke finnes

# Ber brukeren skrive inn en by, og hvis ingen by oppgis, brukes "Oslo"
city = input("Skriv inn en by, f.eks. Oslo: ") or "Oslo"
weather = get_weather(city)  # Kaller funksjonen for å hente værdata
print(weather)  # Skriver ut værdataene
