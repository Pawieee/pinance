import requests
from datetime import datetime, timedelta
import pandas as pd

# Your API key
api_key = '04E756C4-B74B-4297-9CBA-B2197109A365'

# Symbol ID for Bitcoin in USD (replace with the actual symbol ID if different)
symbol_id = 'BITSTAMP_SPOT_BTC_USD'

# Calculate the date one month ago and the current date
one_month_ago = datetime.now() - timedelta(days=30)
one_month_ago_str = one_month_ago.strftime('%Y-%m-%dT%H:%M:%S')
current_date_str = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

# Set up the request URL and headers
url = f'https://rest.coinapi.io/v1/ohlcv/{symbol_id}/history'
headers = {
    'Accept': 'application/json',
    'X-CoinAPI-Key': api_key
}

# Set up the query parameters
params = {
    'period_id': '1HRS',  # Change to 1DAY to get daily data for the last month
    'time_start': one_month_ago_str,
    'time_end': current_date_str,
    'limit': 1000 # change to get more data
}

# Make the request
response = requests.get(url, headers=headers, params=params)

# Check the response status and print the data
if response.status_code == 200:
    data = response.json()
    # Create a dataframe to store the data
    df = pd.DataFrame(data)

    # Print the dataframe
    print(df[['time_period_start', 'time_open', 'price_open', 'price_high', 'price_low', 'price_close']])

else:
    print(f"Error: {response.status_code}, {response.text}")