from parser.market_parser import MarketParser

with open("market.html", "r", encoding="utf-8") as f:
    html = f.read()

parser = MarketParser()

items = parser.parse(html)

print(f"Total item: {len(items)}")

for item in items[:5]:

    print("=" * 50)
    print(f"Name      : {item.name}")
    print(f"Category  : {item.category}")
    print(f"Price     : {item.price}")
    print(f"Quantity  : {item.quantity}")
    print(f"URL       : {item.market_url}")