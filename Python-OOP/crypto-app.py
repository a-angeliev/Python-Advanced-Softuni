from requests import Request, Session
import json
import pprint


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

bitcoin_quantity = 0.03891678 + 0.00285+ 0.00394
ethereum_quantity = 0.36456444 + 0.12512345548 + 0.15615394 + 0.02472922
polkadot_quantity = 19.94983 + 6.42458836
bitcoin_parameters = {
    'slug': 'bitcoin',
    'convert': 'USD'
}

ethereum_parameters = {
    'slug': 'ethereum',
    'convert': 'USD'
}

polkadot_parameters = {
    'slug': 'polkadot',
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b78848e1-0658-48e2-85f1-f9d1c769ffee'
}

session = Session()
session.headers.update(headers)

bitcoin_response = session.get(url, params = bitcoin_parameters)
# pprint.pprint(json.loads(bitcoin_response.text)["data"]["1"]["quote"]["USD"]["price"])
bitcoin_price = json.loads(bitcoin_response.text)["data"]["1"]["quote"]["USD"]["price"]

ethereum_response = session.get(url, params = ethereum_parameters)
# pprint.pprint(json.loads(ethereum_response.text)["data"]['1027']['quote']["USD"]["price"])
ethereum_price = json.loads(ethereum_response.text)["data"]['1027']['quote']["USD"]["price"]

polkadot_response = session.get(url, params = polkadot_parameters)
# pprint.pprint(json.loads(polkadot_response.text)["data"]['6636']['quote']["USD"]["price"])
polkadot_price = json.loads(polkadot_response.text)["data"]['6636']['quote']["USD"]["price"]

all_usd = polkadot_price * polkadot_quantity + ethereum_price * ethereum_quantity + bitcoin_quantity * bitcoin_price
print(f"Portfolio in %:")
print(f"BTC: {(bitcoin_price * bitcoin_quantity)/all_usd*100:.0f}%")
print(f"ETH: {(ethereum_price * ethereum_quantity)/all_usd*100:.0f}%")
print(f"DOT: {(polkadot_price * polkadot_quantity)/all_usd*100:.0f}%")
print(f"/////////////////")
print(f"Crypto in USD:")
print(f"BTC in USD: {(bitcoin_price * bitcoin_quantity):.0f}$")
print(f"ETH in USD: {(ethereum_price * ethereum_quantity):.0f}$")
print(f"DOT in USD: {(polkadot_price * polkadot_quantity):.0f}$")
print("//////////////////")
print(f"All money:")
print(f"ALL in USD: {all_usd:.0f}$")
print(f"ALL in BGN: {(all_usd * 1.68):.0f}")

