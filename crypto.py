from pycoingecko import CoinGeckoAPI
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go

# Initialize CoinGeckoAPI
cg = CoinGeckoAPI()

# Define the cryptocurrency and date range
currency = 'bitcoin'
vs_currency = 'usd'
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Convert dates to Unix timestamps
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())

# Get historical market data for Bitcoin
historical_data = cg.get_coin_market_chart_range_by_id(
    id=currency,
    vs_currency=vs_currency,
    from_timestamp=start_timestamp,
    to_timestamp=end_timestamp
)

# Convert the data to a DataFrame
prices = historical_data['prices']
volumes = historical_data['total_volumes']

df_prices = pd.DataFrame(prices, columns=['timestamp', 'price'])
df_volumes = pd.DataFrame(volumes, columns=['timestamp', 'volume'])

# Convert the timestamp to a readable date format
df_prices['date'] = pd.to_datetime(df_prices['timestamp'], unit='ms')
df_volumes['date'] = pd.to_datetime(df_volumes['timestamp'], unit='ms')

# Set the date as the index
df_prices.set_index('date', inplace=True)
df_volumes.set_index('date', inplace=True)

# Drop the timestamp column
df_prices.drop(columns=['timestamp'], inplace=True)
df_volumes.drop(columns=['timestamp'], inplace=True)

# Resample the data to daily frequency and calculate OHLCV values
df_ohlc = df_prices['price'].resample('D').ohlc()
df_ohlc['volume'] = df_volumes['volume'].resample('D').sum()

# Print the DataFrame
print(df_ohlc)

# Plot the candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df_ohlc.index,
    open=df_ohlc['open'],
    high=df_ohlc['high'],
    low=df_ohlc['low'],
    close=df_ohlc['close'],
    increasing_line_color='green',
    decreasing_line_color='red'
)])

# Update layout for better visualization
fig.update_layout(
    title='BTC to USD Candlestick Chart',
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    xaxis_rangeslider_visible=False
)

# Show the chart
fig.show()