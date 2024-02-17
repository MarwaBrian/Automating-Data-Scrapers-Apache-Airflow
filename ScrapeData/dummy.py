import requests
from bs4 import BeautifulSoup
import csv
import json
import random
import time

# Base URL for the website
BASE_URL = "https://example.com"

# URL template for the listings
url_template = "https://example.com/listings?page={}"

# end_page variable
end_page = 179

# Open the CSV file in append mode
with open("house_listings.csv", "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    for page in range(1, end_page + 1):
        response = requests.get(url_template.format(page))
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all elements matching the provided XPath
        listing_elements = soup.find_all(xpath="/html/body/div[2]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[3]/div/div[2]/div/div[1]/div/span/div[2]/div/div/div[2]/div[1]/div[1]/h3[1]/a/span")

        for element in listing_elements:
            # Extract href attribute
            href = element.get("href")
            if not href:
                print("Href attribute not found for a listing")
                continue

            # Extract JSON data
            json_data = {}
            for attribute, value in element.attrs.items():
                if "wire:click.prevent" in value:
                    json_data = json.loads(value.split(",")[-2])
                    break

            if not json_data:
                print("JSON data not found for a listing")
                continue

            item_name = json_data.get("item_name")
            price = json_data.get("itemPrice")
            location = json_data.get("propertyArea")
            status = json_data.get("propertyStatus")

            # Extracting the location and unique ID from the href
            location_id = href.split("-rent-")[1]
            unique_id, location_name = location_id.split("-", 1)

            # Write data to CSV file
            writer.writerow([item_name, price, location_name, unique_id, status, BASE_URL + href])

        # Introduce a random delay before scraping subsequent pages
        time.sleep(random.uniform(1, 3))

