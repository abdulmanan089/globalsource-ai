import requests
from bs4 import BeautifulSoup

def search_alibaba(product):

    url = f"https://www.alibaba.com/trade/search?SearchText={product}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    suppliers = []

    items = soup.find_all("h2")

    for item in items[:10]:

        title = item.get_text(strip=True)

        suppliers.append({
            "product": title,
            "price": "Unknown",
            "moq": "Unknown",
            "rating": "Unknown"
        })

    return suppliers