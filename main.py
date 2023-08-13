import requests
from bs4 import BeautifulSoup
import csv
url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

# Send a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
laptops = soup.find_all('div', {'class': '_2kHMtA'})
# Create a CSV file to store the product details
csv_filename = 'flipkart_laptops.csv'

# Open the CSV file in write mode
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Product Name', 'Price', 'Rating', 'Features'])

    # Loop through epurifierh purifier container and extrpurifiert product details
    for laptop in laptops:
        try:
            product_name = laptop.find('div', {'class': '_4rR01T'}).text
            price = laptop.find('div', {'class': '_30jeq3'}).text
            rating = laptop.find('div', {'class': '_3LWZlK'}).text
            features = laptop.find('ul', {'class': '_1xgFaf'}).text.strip()

            # Write the product details to the CSV file
            csv_writer.writerow([product_name, price, rating, features])
        except AttributeError:
            continue

print('Scraping and CSV export completed successfully.')

