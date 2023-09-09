import sqlite3
import requests
from datetime import datetime

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS links (
                    id INTEGER PRIMARY KEY,
                    link VARCHAR(100),
                    name VARCHAR(20)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS money (
                    id INTEGER PRIMARY KEY,
                    currency FLOAT,
                    hrn FLOAT,
                    result FLOAT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY,
                    date DATETIME,
                    result VARCHAR(100)
                )''')

conn.commit()


def get_current_exchange_rate():
    response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json")
    data = response.json()
    exchange_rate = float(data[0]["rate"])
    return exchange_rate


def buy_currency():
    try:
        amount = float(input("Введіть суму у гривнях: "))
        exchange_rate = get_current_exchange_rate()
        result = round(amount / exchange_rate, 2)

        cursor.execute("INSERT INTO money (currency, hrn, result) VALUES (?, ?, ?)",
                       (exchange_rate, amount, result))
        conn.commit()

        print(f"Ви отримаєте {result} USD за {amount} гривень за поточним курсом {exchange_rate}")
    except ValueError:
        print("Будь ласка, введіть коректну суму.")


def get_weather():
    date_str = input("Введіть дату (у форматі YYYY-MM-DD HH:MM): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        weather_data = "Погода зараз гарна"
        cursor.execute("INSERT INTO weather (date, result) VALUES (?, ?)",
                       (date, weather_data))
        conn.commit()
        print(f"Погода на {date}: {weather_data}")
    except ValueError:
        print("Будь ласка, введіть коректний формат дати.")


while True:
    print("Виберіть необхідну опцію:")
    print("1 - купівля валюти у NBU")
    print("2 - температура повітря у Києві")
    print("0 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        buy_currency()
    elif choice == "2":
        get_weather()
    elif choice == "0":
        break
    else:
        print("Будь ласка, виберіть коректну опцію.")

conn.close()