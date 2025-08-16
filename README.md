# Shopify Insights Tool

This small Python tool fetches a Shopify store's HTML and extracts common pieces of information (products, hero/featured products, policies, social links, contact details, and more).

Usage
-

1. Install requirements:

```bash
python -m pip install -r requirements.txt
```

2. Run the CLI:

```bash
python main.py https://examplestore.myshopify.com
```

If you don't pass a URL on the command line the script will prompt for one.

Files added
-

- `fetcher.py` — Fetches the HTML and calls the parser.
- `parser.py` — Extracts insights using BeautifulSoup.
- `main.py` — CLI entrypoint that prints JSON output.
- `requirements.txt` — Python dependencies.
- `tests/test_parser.py` — Basic pytest tests for parsing helpers.

Development
-

- Run tests with `pytest`.
- Improve parsing selectors in `parser.py` to support additional Shopify themes.

License
-

No license specified. Add LICENSE if you want to make this project public.