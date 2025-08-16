import sys
from fetcher import fetch_store_data

def main(store_url):
    data = fetch_store_data(store_url)
    print(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <shopify_store_url>")
    else:
        main(sys.argv[1])