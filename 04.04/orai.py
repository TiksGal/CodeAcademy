import re
import requests
from bs4 import BeautifulSoup

url = "https://orai.15min.lt/prognozes"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Ieškome oro prognozės Vilniuje
    vilnius_forecast = soup.find("a", href=re.compile("/prognozes/Vilnius"))

    if vilnius_forecast:
        # Ištraukiame informaciją apie temperatūrą ir orą
        temperature = vilnius_forecast.find("span", class_="temp")
        weather_condition = vilnius_forecast.find("span", class_="condition")

        # Atspausdiname rezultatą
        print(f"Oro prognozė Vilniuje šiuo metu: {temperature.text}, {weather_condition.text}")
    else:
        print("Vilniaus oro prognozės nerasta.")
else:
    print("Nepavyko gauti informacijos iš svetainės")
