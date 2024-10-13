from bs4 import BeautifulSoup
import requests
a = []
response = requests.get("https://minfin.com.ua/ua/currency/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    soup_list = soup.find_all('div', class_='sc-1x32wa2-9 bKmKjX')
    for element in soup_list:
        a.append(element.text.strip())
print(a[0])

f = a[0].replace(',', '').strip()
r = float(f)
print('f - ',f)
r = r/100000
print('r - ',r)
b = float(input("Введіть суму гривень: "))
c = b / r
print("В еквіваленті доларів: $", c)
