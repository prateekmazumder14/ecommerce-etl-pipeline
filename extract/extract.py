import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def extract_products():
    base_url = os.getenv("API_URL")
    url = f"{base_url}/products"

    print(f"Calling: {url}")
    response = requests.get(url)
    response.raise_for_status()

    products = response.json()
    print(f"Got {len(products)} Products")
    with open("raw_products.json", "w") as f:
        json.dump(products, f, indent=2)
    print("Saved raw_products.json")

    return products

if __name__ == "__main__":
    extract_products()