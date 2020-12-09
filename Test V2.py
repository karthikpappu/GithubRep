import alpaca_trade_api as tradeapi

# authentication and connection details
api_key = 'PKPHLT0V9WFI4Y7AY442'
api_secret = '1sEnfWFWrYD1cy7PM5X54JQP85zIkkIAJDPIdVWp'
base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()
assert isinstance(account, object)
print(account)