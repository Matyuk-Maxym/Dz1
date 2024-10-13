import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def create_database():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Weather (date TEXT,temperature REAL)''')
    conn.commit()
    conn.close()

def get_temperature(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_temperature_element = soup.find_all('temperature-value', class_='value')
    for temperature_element in soup_temperature_element:
        return float(temperature_element.text)
    else:
        print("Нічого не знайдено.")
        return None

def insert_temperature(date, temperature):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('INSERT INTO Weather (date, temperature) VALUES (?, ?)', (date, temperature))
    conn.commit()
    conn.close()



def main():
    create_database()
    url = 'https://meteofor.com.ua/'
    temperature = get_temperature(url)
    if temperature is not None:
        current_date = datetime.now().strftime('%Y-%m-%d')
        insert_temperature(current_date, temperature)
        print(f"Дані внесено: {current_date}, температура: {temperature}°C")

if __name__ == '__main__':
    main()
