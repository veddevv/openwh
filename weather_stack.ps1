# Spør brukeren hvor de bor
$city = Read-Host "Hvor bor du? Skriv inn bynavn"

# Koordinater for norske byer
$coordinates = @{
    "Oslo" = @(59.91, 10.75)
    "Bergen" = @(60.39, 5.32)
    "Trondheim" = @(63.43, 10.39)
    "Stavanger" = @(58.97, 5.73)
    "Tromsø" = @(69.65, 18.96)
    "Kristiansand" = @(58.15, 8.00)
    "Drammen" = @(59.74, 10.20)
    "Ålesund" = @(62.47, 6.15)
    "Bodø" = @(67.28, 14.40)
    "Tønsberg" = @(59.27, 10.41)
    "Arendal" = @(58.46, 8.77)  # Arendal lagt til
}

# Sjekker om byen finnes i koordinatene
if ($coordinates.ContainsKey($city)) {
    $latitude, $longitude = $coordinates[$city]  # Henter bredde- og lengdegrad
    $url = "https://api.open-meteo.com/v1/forecast?latitude=$latitude&longitude=$longitude&current_weather=true"  # Bygger URL
    $response = Invoke-RestMethod -Uri $url  # Sender forespørsel til API
    $weather = $response.current_weather  # Henter værdata
    Write-Output "Værdata for $city: Temperatur: $($weather.temperature)°C, Vind: $($weather.windspeed) km/t"  # Skriver ut værdata
} else {
    Write-Output "Byen er ikke tilgjengelig i databasen"
}
