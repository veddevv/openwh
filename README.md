# OpenWH

## Om Prosjektet
OpenWH er en samling av skript (PowerShell og Python) som henter værdata fra Open-Meteo API. Skriptene gir deg rask tilgang til værinformasjon direkte fra kommandolinjen, med mulighet for å velge mellom to forskjellige implementasjoner basert på dine preferanser eller systembegrensninger.

## Funksjonalitet
- Henter værdata fra Open-Meteo API
- Viser:
  - Nåværende værforhold
  - Temperatur
  - Nedbørsinformasjon
  - Vinddata
- Tilgjengelig i både PowerShell og Python

## Forskjeller mellom implementasjonene

### PowerShell-versjon
- Optimalisert for Windows-miljøer
- Bruker native PowerShell-kommandoer for HTTP-requests
- Formaterer output med PowerShell-spesifikke formateringsverktøy
- Bedre integrasjon med Windows-spesifikke funksjoner

### Python-versjon
- Plattformuavhengig (kjører på Windows, macOS, Linux)
- Bruker requests-biblioteket for HTTP-forespørsler
- Mer fleksibel databehandling
- Lettere å utvide med additional Python-biblioteker

## Teknisk Informasjon
- PowerShell script (.ps1)
- Python script (.py)
- Bruker Open-Meteo API for værdata
- Ingen ekstra rammeverk eller biblioteker

## Forutsetninger

### For PowerShell
- Windows med PowerShell 5.1 eller nyere
- Internettilkobling
- PowerShell må være konfigurert til å kunne kjøre skript:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### For Python
- Python 3.x installert
- Standard Python-biblioteker
- Internettilkobling

## Installasjon
1. Klon repositoriet:
```bash
git clone https://github.com/veddevv/openwh.git
```

2. Naviger til skriptmappen:
```bash
cd openwh
```

## Bruk

### PowerShell
```powershell
# Grunnleggende bruk
.\weather_stack.ps1

# Med spesifikke koordinater
.\weather_stack.ps1 -Latitude 59.9139 -Longitude 10.7522

# Med alle valgfrie parametre
.\weather_stack.ps1 -Latitude 59.9139 -Longitude 10.7522 -Detailed
```

### Python
```bash
# Grunnleggende bruk
python weather_stack.py

# Med spesifikke koordinater
python weather_stack.py --lat 59.9139 --lon 10.7522

# Med alle valgfrie parametre
python weather_stack.py --lat 59.9139 --lon 10.7522 --detailed
```

## Eksempel på Output

### PowerShell Output
```
Værdata for Oslo, Norge:
Temperatur: 18°C
Vindstyrke: 5 m/s
Nedbør: 0 mm
Luftfuktighet: 65%

Detaljert informasjon (hvis --detailed er brukt):
UV-indeks: 5.2
Skydekke: 25%
Lufttrykk: 1013 hPa
```

### Python Output
```
Weather data for Oslo, Norway:
Temperature: 18°C
Wind Speed: 5 m/s
Precipitation: 0 mm
Humidity: 65%

Detailed information (if --detailed is used):
UV Index: 5.2
Cloud Cover: 25%
Air Pressure: 1013 hPa
```

## Kommandolinjeargumenter

### PowerShell Parametre
- `-Latitude`: Breddegrad (valgfri, standard: Oslo)
- `-Longitude`: Lengdegrad (valgfri, standard: Oslo)
- `-Detailed`: Vis detaljert værinformasjon (switch parameter)

### Python Argumenter
- `--lat`: Breddegrad (valgfri, standard: Oslo)
- `--lon`: Lengdegrad (valgfri, standard: Oslo)
- `--detailed`: Vis detaljert værinformasjon (flag)

## Feilsøking

### Vanlige PowerShell-problemer

1. **Execution Policy Error**
```powershell
# Feilmelding:
"Execution of scripts is disabled on this system"

# Løsning:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. **Nettverksproblemer**
```powershell
# Sjekk internettforbindelse
Test-NetConnection open-meteo.com -Port 443
```

### Vanlige Python-problemer

1. **ModuleNotFoundError**
```bash
# Feilmelding:
ModuleNotFoundError: No module named 'requests'

# Løsning:
pip install requests
```

2. **Permission Error** (Linux/macOS)
```bash
# Feilmelding:
Permission denied

# Løsning:
chmod +x weather_stack.py
```

### Generell Feilsøking
1. Sjekk at du har internettilkobling
2. Verifiser at koordinatene er gyldige
3. Sjekk at API-endepunktet er tilgjengelig
4. Se etter feilmeldinger i konsollen

## Kjente Begrensninger
- API-rategrenser fra Open-Meteo
- Nøyaktighet avhenger av tilgjengelige værstasjoner
- Enkelte værdata kan mangle for noen lokasjoner

## Lisens
Dette prosjektet er lisensiert under GNU General Public License v3.0 (GPL-3.0).

### Hva dette betyr:
- ✔️ Du kan kommersielt bruke dette prosjektet
- ✔️ Du kan modifisere og distribuere prosjektet
- ✔️ Du kan bruke prosjektet for private formål
- ✔️ Du kan patentere modifikasjoner du gjør
- ❗ Du må publisere kildekoden når du distribuerer prosjektet
- ❗ Du må inkludere den originale lisensen
- ❗ Du må dokumentere endringer du gjør
- ❗ Du må lisensiere modifikasjoner under GPL-3.0

For full lisensinformasjon, se [LICENSE](LICENSE) filen i prosjektet eller besøk [GNU GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Anerkjennelser
- [Open-Meteo](https://open-meteo.com/) for værdatatjenesten
- Bidragsytere til prosjektet

## Kontakt
For spørsmål eller problemer, vennligst åpne en issue på GitHub.
