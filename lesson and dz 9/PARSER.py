import requests

response = requests.get("https://coinmarketcap.com/")
response_parse = response.text.split("<span>")


for page in response_parse:
    if page.startswith("$"):
        for page1 in page.split("</span>"):
            if page1.startswith("$") and page1[1].isdigit():
                print(page1)