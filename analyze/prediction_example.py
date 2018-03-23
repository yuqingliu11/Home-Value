# example showing how time series is applied

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas import Series,DataFrame,DatetimeIndex
from statsmodels.tsa.arima_model import ARIMA
from pandas.tools.plotting import autocorrelation_plot
import statistics
from scipy import stats
from datetime import datetime


# get national mean price
price = pd.read_csv('newdata/Zip_MedianListingPrice_AllHomes.csv',converters={'RegionName': str})
national_mean = price.drop(['RegionName','City','State','Metro','CountyName','SizeRank'],axis=1).mean(axis=0)
dates = national_mean.index


# remove trend and plot vs. original data
data = DataFrame(national_mean.tolist(), DatetimeIndex(start=dates[0],periods=len(dates),freq='M'))
moving_avg = pd.rolling_mean(data,12)
moving_avg.index = national_mean.index
diff = data.values - moving_avg.values
diff = DataFrame([item for sublist in diff for item in sublist])
diff.index = national_mean.index
plt.plot(moving_avg.values)
plt.plot(national_mean.values)
plt.show()

# remove seasonality and plot residual vs. trend residual
diff_clean = diff.dropna()
diff_clean = DataFrame([item for sublist in diff_clean.values for item in sublist], DatetimeIndex(start=dates[0],periods=len(diff_clean),freq='M'))
decomp = seasonal_decompose(diff_clean,freq=12,model="additive")
plt.plot(diff_clean)
plt.plot(decomp.seasonal)
plt.show()
residual = decomp.resid
plt.plot(residual)

# view data
national_mean.head(10)
diff.head(10)
residual.head(10)

# mean and sd of residual
residual_median = residual.median()
residual_sd = statistics.stdev([item for sublist in residual.dropna().values for item in sublist])

# record seasonal component and trend
cycle = [item for sublist in decomp.seasonal.values[-12:] for item in sublist]
last_dates = dates[-24:]
x = range(1,25)
y = [item for sublist in moving_avg.tail(24).values for item in sublist]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# make prediction
test_date = '2018-04'
test_noise = residual_median 
def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month
gap = diff_month(datetime.strptime(test_date, '%Y-%m'),datetime.strptime(last_dates[len(last_dates)-1], '%Y-%m'))
test_trend = intercept + slope * (x[len(x)-1]+gap)
test_season = cycle[gap % 12 - 1]
test_pred = test_noise + test_trend + test_season

