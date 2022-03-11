# importing the libraries you'll need
from cryptocmd import CmcScraper
import yfinance as yf

ticker = yf.Ticker()

# getting the data and exporting it to a csv file
scraper = CmcScraper("BTC", "08-03-2021", "08-03-2022")
df = scraper.get_dataframe()
df.to_csv("BTC_1yr_data.csv")





