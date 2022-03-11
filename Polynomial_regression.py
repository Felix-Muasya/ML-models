import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

df = pd.read_csv("BTC_1yr_data.csv")
x = df["Volume"]
y = df["Close"]

#finding the lowest and highest values of our variables
# print(y.max())
# print(x.max())
# print(x.min())


mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(13736557862.99, 126358098746.69, 67557)

# plotting
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

#checking the r2 score
print("the R2 score is", r2_score(y, mymodel(x)))

# asking the user to input the
vol = int(input("Input the volume: "))
print(mymodel(vol))
