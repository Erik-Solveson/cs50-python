#This is a python script that asks the user for a number of bitcoins and returns the price of that number of the cryptocurrency

import requests
import sys

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
TEST_TRIVIA_URL = "http://jservice.io/api/random"


def main():
#     bitcoin_price = get_current_bitcoin_to_USD_price()
    response = requests.get(API_URL)
    # response.json()
    print(response)

# def get_current_bitcoin_to_USD_price():
#     try:
#         response = requests.get(TEST_TRIVIA_URL)
#         print(response)
#     except requests.RequestException as e:
#         print(f"there was problem with your request {e}")
#     except requests.ConnectTimeout:
#         print(f"Your connection timed out")

main()