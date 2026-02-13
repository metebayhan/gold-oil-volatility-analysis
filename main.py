import pandas as pd
import pandas_datareader.data as web
import pandas_datareader.wb as wb
from datetime import datetime
import numpy as np


gold_prices = pd.read_csv("gold_prices.csv")
crude_oil_prices = pd.read_csv("crude_oil_prices.csv")

gold_prices["Gold_Price"] = pd.to_numeric(
    gold_prices["Gold_Price"], errors="coerce"
)
crude_oil_prices["Crude_Oil_Price"] = pd.to_numeric(
    crude_oil_prices["Crude_Oil_Price"], errors="coerce"
)

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)

gdp_data = wb.download(
    indicator="NY.GDP.MKTP.CD",
    country=["US"],
    start=start,
    end=end
)

export_data = wb.download(
    indicator="NE.EXP.GNFS.CN",
    country=["US"],
    start=start,
    end=end
)

def log_return(prices):
    return np.log(prices / prices.shift(1)).dropna()


gold_returns = log_return(gold_prices["Gold_Price"])
crude_oil_returns = log_return(crude_oil_prices["Crude_Oil_Price"])

print("Gold Variance:", gold_returns.var())
print("Crude Oil Variance:", crude_oil_returns.var())
