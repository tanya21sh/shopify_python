from bs4 import BeautifulSoup
from parser import find_social_links, find_contact_details, parse_html

def test_find_social_links():
    html = '<a href="https://instagram.com/shop">insta</a><a href="https://facebook.com/shop">fb</a>'
    soup = BeautifulSoup(html, 'html.parser')
    res = find_social_links(soup)
    assert 'instagram' in res and res['instagram'].startswith('https://')
    assert 'facebook' in res and res['facebook'].startswith('https://')

def test_find_contact_details():
    html = 'Contact us at test@example.com or +1 555-123-4567'
    soup = BeautifulSoup(html, 'html.parser')
    res = find_contact_details(soup)
    assert 'test@example.com' in res['emails']
    assert any('555' in p for p in res['phones'])

def test_parse_html_minimal():
    html = '<div class="product">Prod A</div><a href="/privacy">Privacy</a>'
    data = parse_html(html, 'https://example.com')
    assert 'products' in data
    assert data['privacy_policy'] == '/privacy'.