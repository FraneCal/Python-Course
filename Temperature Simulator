'''
Napravite aplikaciju koja će generirati nasumične podatke, tako da simulira dnevni rast temperature od jutra do
poslijepodneva i zatim pad do ranog jutra. Podatke treba pohraniti u rječnik, tako da je ključ datum, a podaci
lista parova vrijednosti (tuple) vremena i temperature. Temperatura treba biti izmjerena svakih 15 minuta.

Temperatura zraka od -25 do +39 stupnjeva Celzijusa
Početni datum i vrijeme trebaju biti uneseni od strane korisnika, a moraju biti minimalno dvije godine prije današnjeg datuma.
Podacima se mogu dodati i informacije o vlažnosti zraka (vrijednosti od 15% do 95%) te tlak zraka (990 hPa do 1035 hPa)
'''

import random
from datetime import datetime, timedelta

def generate_temperature_data(year, month, day):
    start_date = datetime(year, month, day, 0, 0)
    temperature_data = {}

    temperature_ranges = {
        1: (-5, 10),   # January
        2: (0, 15),    # February
        3: (5, 20),    # March
        4: (10, 25),   # April
        5: (15, 30),   # May
        6: (20, 35),   # June
        7: (25, 38),   # July
        8: (20, 33),   # August
        9: (15, 28),   # September
        10: (10, 20),  # October
        11: (5, 15),   # November
        12: (0, 10)    # December
    }

    temperature_range = temperature_ranges.get(month, (-5, 38))

    for _ in range(96):
        temperature = round(random.uniform(temperature_range[0], temperature_range[1]), 2)
        time = start_date.strftime('%H:%M')
        temperature_data[start_date.strftime('%Y-%m-%d')] = temperature_data.get(start_date.strftime('%Y-%m-%d'), []) + [(time, temperature)]
        start_date += timedelta(minutes=15)

    return temperature_data


while True:
    try:
        current_year = datetime.now().year
        entered_year = int(input("Enter the year (at least 2 years before the current year): "))
        if entered_year <= current_year - 2:
            current_month = int(input("Enter the current month (1-12): "))
            current_day = int(input("Enter the current day (1-31): "))
            current_date = datetime(current_year, current_month, current_day)
            entered_date = datetime(entered_year, current_month, current_day)
            today = datetime.now()

            if today >= entered_date:
                break
            else:
                print("Please enter a valid date in the past.")
        else:
            print("Please enter a valid year that is at least 2 years before the current year.")
    except ValueError:
        print("Invalid input. Please enter valid values.")

temperature_data = generate_temperature_data(entered_year, current_month, current_day)

for date, data_points in temperature_data.items():
    print(f"Date: {date}")
    for time, temperature in data_points:
        print(f"Time: {time}, Temperature: {temperature}°C")



