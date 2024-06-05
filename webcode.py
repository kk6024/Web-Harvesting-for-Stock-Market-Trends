import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Scrape stock prices from Yahoo Finance
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

stock_prices = []
for row in soup.find_all('tr', {'class': 'BdT Bdc($seperatorColor)'}):
    date = row.find('td', {'class': 'Py(10px)'}).text.strip()
    open_price = row.find('td', {'class': 'Py(10px) Ta(start)'}).text.strip()
    high_price = row.find('td', {'class': 'Py(10px) Ta(start)'}).text.strip()
    low_price = row.find('td', {'class': 'Py(10px) Ta(start)'}).text.strip()
    close_price = row.find('td', {'class': 'Py(10px) Ta(start)'}).text.strip()
    volume = row.find('td', {'class': 'Py(10px) Ta(end)'}).text.strip()
    stock_prices.append({'date': date, 'open': open_price, 'high': high_price, 'low': low_price, 'close': close_price, 'volume': volume})

# Store the data in a Pandas dataframe
df = pd.DataFrame(stock_prices)

# Analyze the data
daily_returns = df['close'].pct_change()
monthly_returns = df['close'].resample('M').last().pct_change()

# Visualize the data
plt.plot(daily_returns)
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.title('Daily Returns of AAPL')
plt.show()

plt.plot(monthly_returns)
plt.xlabel('Date')
plt.ylabel('Monthly Returns')
plt.title('Monthly Returns of AAPL')
plt.show()
