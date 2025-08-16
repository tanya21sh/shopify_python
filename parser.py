from bs4 import BeautifulSoup
import re

def parse_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    data = {}

    # 1. Whole Product Catalog
    data['products'] = [prod.text for prod in soup.find_all(class_=re.compile("product", re.I))]

    # 2. Hero Products
    data['hero_products'] = [hero.text for hero in soup.select('.hero, .featured')]

    # 3. Privacy Policy
    data['privacy_policy'] = find_link(soup, 'privacy')

    # 4. Return, Refund Policies
    data['return_policy'] = find_link(soup, 'return')
    data['refund_policy'] = find_link(soup, 'refund')

    # 5. FAQs
    data['faqs'] = [faq.text for faq in soup.find_all(string=re.compile("FAQ", re.I))]

    # 6. Social Handles
    data['social_handles'] = find_social_links(soup)

    # 7. Contact Details
    data['contact_details'] = find_contact_details(soup)

    # 8. Brand Text
    data['brand_text'] = find_about_text(soup)

    # 9. Important Links
    data['important_links'] = find_important_links(soup)

    return data

def find_link(soup, keyword):
    links = soup.find_all('a', href=True)
    for link in links:
        if keyword.lower() in link.text.lower() or keyword.lower() in link['href'].lower():
            return link['href']
    return None

def find_social_links(soup):
    socials = {}
    for a in soup.find_all('a', href=True):
        url = a['href']
        for platform in ['instagram', 'facebook', 'twitter', 'tiktok']:
            if platform in url:
                socials[platform] = url
    return socials

def find_contact_details(soup):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', soup.get_text())
    phones = re.findall(r'\+?\d[\d \-]{8,}\d', soup.get_text())
    return {'emails': emails, 'phones': phones}

def find_about_text(soup):
    # Look for "About Us" section
    about = soup.find(string=re.compile("About", re.I))
    return about.parent.text if about else ""

def find_important_links(soup):
    links = {}
    for a in soup.find_all('a', href=True):
        if any(k in a.text.lower() for k in ['order', 'track', 'contact', 'blog']):
            links[a.text] = a['href']
    return links
