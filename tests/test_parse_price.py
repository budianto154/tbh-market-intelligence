from parser.market_parser import MarketParser

def test_parse_price():

    parser = MarketParser()

    assert parser._parse_price(
        "IDR 12,490"
    ) == 12490

    assert parser._parse_price(
        "IDRÂ 2,249"
    ) == 2249

    assert parser._parse_price("") == 0