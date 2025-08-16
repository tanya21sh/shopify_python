import argparse
import logging
import json
from fetcher import fetch_store_data

def main():
    parser = argparse.ArgumentParser(description="Fetch and print Shopify store insights.")
    parser.add_argument('url', nargs='?', help='Shopify store URL (e.g. https://examplestore.com)')
    args = parser.parse_args()

    if not args.url:
        args.url = input("Enter Shopify store URL: ").strip()

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    logging.info('Fetching store data for %s', args.url)

    try:
        data = fetch_store_data(args.url)
    except Exception as e:
        logging.error('Unhandled error while fetching store data: %s', e)
        raise

    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()