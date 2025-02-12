#This is a python script that asks the user for a number of bitcoins and returns the price of that number of the cryptocurrency

import requests
import sys

API_URL = "http://api.coindesk.com/v1/bpi/currentprice"
ALT_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
TEST_TRIVIA_URL = "http://jservice.io/api/random"


def main():
    bitcoin_price = get_current_bitcoin_to_USD_price()
    print_bitcoin_amount(bitcoin_price)

def get_current_bitcoin_to_USD_price():
    try:
        response = requests.get(ALT_URL)
        data = response.json()
        return data['bitcoin']['usd']
    except requests.RequestException as e:
        print(f"there was problem with your request {e}")
    except requests.ConnectTimeout:
        print(f"Your connection timed out")

def print_bitcoin_amount(bitcoin_price):
    try:
        number = float(sys.argv[1])
        print(f"${number*bitcoin_price:,.4f}")
    except ValueError:
        print("incorrect number of command line args")
        sys.exit()

main()