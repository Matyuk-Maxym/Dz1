import requests
from bs4 import BeautifulSoup
import sqlite3

class DatabaseManager:
    def __init__(self, db_name='sites.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS sites (id INTEGER PRIMARY KEY, url TEXT)''')
            conn.commit()

    def add_site(self, url):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO sites (url) VALUES (?)', (url,))
            conn.commit()

    def clear_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sites')
            conn.commit()

    def get_sites(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT url FROM sites')
            return [url for (url,) in cursor.fetchall()]

class WebParser:
    def search_text(self, query, urls):
        results = []
        for url in urls:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()
                count = text.lower().count(query.lower())
                if count > 0:
                    results.append((url, count))
            except Exception as e:
                print(f'Error fetching {url}: {e}')
        results.sort(key=lambda x: x[1], reverse=True)
        return results

class UserInterface:
    def __init__(self, db_manager, web_parser):
        self.db_manager = db_manager
        self.web_parser = web_parser

    def run(self):
        while True:
            print("\n1. Додати сайт")
            print("2. Очищення бази даних")
            print("3. Пошук")
            print("4. Вихід")
            choice = input("Виберіть опцію: ")

            if choice == '1':
                url = input("Введіть URL сайту: ")
                self.db_manager.add_site(url)
                print(f"Сайт {url} додано.")
            elif choice == '2':
                self.db_manager.clear_db()
                print("Базу даних очищено.")
            elif choice == '3':
                query = input("Введіть текст для пошуку: ")
                urls = self.db_manager.get_sites()
                results = self.web_parser.search_text(query, urls)
                for url, count in results:
                    print(f'{url}: {count} входжень')
            elif choice == '4':
                break
            else:
                print("Неправильний вибір, спробуйте ще раз.")

def run():
    db_manager = DatabaseManager()
    web_parser = WebParser()
    user_interface = UserInterface(db_manager, web_parser)
    user_interface.run()

if __name__ == "__main__":
    run()
