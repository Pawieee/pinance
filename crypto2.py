import requests

# Your API key
api_key = '04E756C4-B74B-4297-9CBA-B2197109A365'

# Set up the request URL and headers
url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = {'X-CoinAPI-Key': api_key}

# Make the request
response = requests.get(url, headers=headers)

# Check the response status and print the data
if response.status_code == 200:
    data = response.json()
    print(f"1 BTC = {data['rate']} USD")
else:
    print(f"Error: {response.status_code}, {response.text}")
