import pandas as pd
from sklearn import linear_model
df = pd.read_csv("BTC_1yr_data.csv")
x = df[["Volume", "Market Cap"]]
y = df["Close"]

regr = linear_model.LinearRegression()
regr.fit(x, y)

# checking te correlation & coovariance betweeen market cap and volume
print(x.corr())
print("\n", x.cov())

# Checking the predicted close, given the volume and market cap
predicted_close = regr.predict([[25776583476, 7.35156E+11]])
print("\n", predicted_close)