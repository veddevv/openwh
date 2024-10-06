# Openwh


## Værapp med Weatherstack API

Dette prosjektet er en enkel værapp som bruker Weatherstack API for å hente værdata og vise dem på en brukervennlig måte. Applikasjonen består av et PowerShell-skript og et Python-skript som sammen gir deg muligheten til å sjekke været i en valgt by.

openwh er kun for Windows foreløpig. openwh får oppdateringer etterhvert, sånn at prosjektet ikke blir dødt.

### Funksjoner

- Hent værdata for en valgt by.
- Vis temperatur, fuktighet og en beskrivelse av været.

### Hvordan Det Fungerer

1. PowerShell-skript (`weather_stack.ps1`):
   - Spør brukeren om bynavn.
   - Kaller Python-skriptet og sender bynavnet som parameter.

2. Python-skript (`weather_stack.py`):
   - Mottar bynavnet fra PowerShell-skriptet.
   - Sender en forespørsel til Weatherstack API for å hente værdata.
   - Viser værdata med temperatur, fuktighet og værbeskrivelse.

### Forutsetninger

- Python 3.x installert.
- En API-nøkkel fra Weatherstack. [Registrer deg her](https://weatherstack.com/) for å få en gratis API-nøkkel.
- PowerShell (for å kjøre PowerShell-skriptet).

### Komme I Gang

1. Klone Repository

   Klon dette prosjektet til din lokale maskin ved å bruke:

   ```
   git clone https://github.com/veddevv/openwh.git
   ```

2. Installer Avhengigheter

   Sørg for at `requests`-biblioteket er installert for Python-skriptet:

   ```
   pip install requests
   ```

3. Konfigurer API-nøkkel

   Åpne `weather_stack.py` og erstatte `din_weatherstack_api_nøkkel` med din egen API-nøkkel fra Weatherstack.

   ```
   api_key = "din_weatherstack_api_nøkkel"
   ```

4. Kjør Applikasjonen

   - Kjør PowerShell-skriptet for å starte værappen:

     ```
     ./weather_stack.ps1
     ```

   - Følg instruksjonene for å oppgi bynavn og få værdata.

### Eksempler på Bruk

Når du bruker appen, vil du få en utskrift som viser værdata for den valgte byen. Her er et eksempel på hva du kan forvente:

```
Været i Oslo:
Temperatur: 15°C
Fuktighet: 67%
Beskrivelse: Klarvær
```

### Bidra

Hvis du ønsker å bidra til dette prosjektet, er du velkommen til å sende pull requests eller åpne issues med forslag til forbedringer. Vi setter pris på all tilbakemelding og forslag som kan hjelpe oss med å gjøre prosjektet enda bedre. Enten det er nye funksjoner, feilrettinger eller bare generelle kommentarer, er vi åpne for å høre fra deg.

### Lisens

Dette prosjektet er lisensiert under GNU General Public License v3.0 (GPL-3.0). Se [LICENSE](https://github.com/veddevv/openwh?tab=GPL-3.0-1-ov-file).

