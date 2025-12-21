import requests
from bs4 import BeautifulSoup
import csv



# Step 1: Fetch webpage
url = "https://quotes.toscrape.com"
response = requests.get(url)
print(response.status_code)

# Step 2: Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find all quotes
quotes = soup.find_all('span', class_= 'text')
authors = soup.find_all('small', class_='author')


# Step 4: Print them
print(f"\n🎯 found {len(quotes)} quotes:\n")

for i, (quote,author) in enumerate(zip(quotes,authors),1):
    print(f"{i} , {quote.text}")
    print(f"  - {author.text}")
    print()

print("✓ Scraping Successful!")

# Save to CSV
with open('quotes.csv','w', newline= '', encoding ='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Quote','Author']) # Header

    for quote, author in zip(quotes,authors):
        writer.writerow([quote.text, author.text])

print("✅ Saved to quotes.csv")




