import requests
from parser import parse_html

def fetch_store_data(store_url):
    response = requests.get(store_url)
    if response.status_code == 200:
        html = response.text
        return parse_html(html, store_url)
    else:
        return {"error": "Failed to fetch URL"}