import requests
from bs4 import BeautifulSoup
import csv



url = 'https://aws.amazon.com/jp/products/'

html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

services = soup.select(".lb-content-item")

file = r'.\list.csv'
with open(file, 'w', newline="", encoding="utf8") as f:
    writer = csv.writer(f)

    for service in services:
        service_name = service.a.span.text
        detail = service.a.cite.text
        
        row = [service_name, detail]
        print(row)

        writer.writerow(row)


