import requests


def get_last_price(ticker: str) -> float:

    """
    Esta funcion busca usando la API de yahoo finance el ultimo precio disponible del isntrumento cuyo ticker es 'ticker'
    @:param ticker: ticker de la empresa a consultor
    """
    yahoo_finance_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    # url = f"https://query1.finance.yahoo.com/v8/finance/chart/NFLX?" + ticker #lo mismo que arriba pero más cutre
    headers = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=yahoo_finance_url, headers=headers)
    if r.json().get('result') is None:
        raise ValueError(F"ticker: '{ticker}' not found")

    price = r.json().get('chart').get('result')[0].get('meta').get('regularMarketPrice')
    return price

