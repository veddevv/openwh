# Spør brukeren hvor de bor
$city = Read-Host "Hvor bor du? Skriv inn bynavn"
# Kall Python for å hente værdata basert på brukerens by
python weather_stack.py $city
