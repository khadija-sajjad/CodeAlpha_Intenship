import requests
from bs4 import BeautifulSoup
import pandas as pd
books = []
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.encode("latin1").decode("utf-8")
        rating = book.p["class"][1]      
        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })
    print(f"Page {page} done!")
df = pd.DataFrame(books)
print(f"\nTotal books scraped: {len(df)}")
df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")
print("Data saved to books_data.csv!")