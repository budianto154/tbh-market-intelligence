from parser.market_parser import MarketParser

def test_parse_market():

    with open("market.html", encoding="utf-8") as f:
        html = f.read()

    parser = MarketParser()

    items = parser.parse(html)

    assert len(items) == 30

    assert items[0].price > 0

    assert items[0].name != ""