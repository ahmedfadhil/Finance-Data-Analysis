import datetime as dt
import pandas as pd
import numpy as np
from matplotlib import style
import pandas_datareader as web
import matplotlib.pyplot as plt

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

# df = web.DataReader('TSLA', 'yahoo', start, end)
# df = web.get_data_yahoo('GOOG', start, end)﻿
df = web.DataReader("NASDAQ:TSLA", 'google', start, end)

print(df.head(20))

plt.plot(df)
plt.show()