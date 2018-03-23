# import packages
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


# decompose data into trend + easonality + noise
def timeseries_decompose(zipcode):
    # get data by zipcode
    price = pd.read_csv('newdata/Zip_MedianListingPrice_AllHomes.csv',converters={'RegionName': str})
    data = price.loc[price['RegionName'] == zipcode]
    data = data.drop(['RegionName','City','State','Metro','CountyName','SizeRank'],axis=1)
    prices = [item for sublist in data.values for item in sublist]
    prices = prices[np.isnan(prices).sum():]
    dates = data.columns.values[-len(prices):]
    n = len(dates)
    # when fewer than 36 month data, not enough for construct 2 cycles of seasoanl component after differencing
    if (n<36):
        return("not enough data for this region")
    else:
        prices = pd.Series(prices)
        prices.index = dates
        
        # remove trend and plot vs. original data
        data_clean = DataFrame(prices.tolist(), DatetimeIndex(start=dates[0],periods=len(dates),freq='M'))
        moving_avg = pd.rolling_mean(data_clean,12)
        moving_avg.index = prices.index
        diff = data_clean.values - moving_avg.values
        diff = DataFrame([item for sublist in diff for item in sublist])
        diff.index = prices.index

        # remove seasonality and plot residual vs. trend residual
        diff_clean = diff.dropna()
        diff_clean = DataFrame([item for sublist in diff_clean.values for item in sublist], DatetimeIndex(start=dates[0],periods=len(diff_clean),freq='M'))
        decomp = seasonal_decompose(diff_clean,freq=12,model="additive")
        residual = decomp.resid
        
        # mean and sd of residual
        residual_median = residual.median()
        residual_sd = statistics.stdev([item for sublist in residual.dropna().values for item in sublist])
        
        # record seasonal component and trend
        cycle = [item for sublist in decomp.seasonal.values[-12:] for item in sublist]
        last_dates = dates[-24:]
        x = range(1,25)
        y = [item for sublist in moving_avg.tail(24).values for item in sublist]
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        parameters = [zipcode]+[residual_median[0]]+[residual_sd]+[intercept]+[slope]+cycle
        return(parameters)


if __name__ == '__main__':
    # save decompositon of all zipcodes
    price = pd.read_csv('newdata/Zip_MedianListingPrice_AllHomes.csv',converters={'RegionName': str})
    zips = price['RegionName']
    all_parameters = [[]]
    for i in range(len(zips)):
         zipcode = zips[i]
         zip_parameters = timeseries_decompose(zipcode)
         if (type(zip_parameters)!=str):
              all_parameters.append(zip_parameters)
         if (i % 100 ==0):
              print(i)
    all_parameters =  all_parameters[1:len(all_parameters)]
    all_parameters = DataFrame(all_parameters,columns=["zipcode","residual_median","residual_sd","intercept","slope","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11","c12",])    
    all_parameters.to_csv("base_parameters.csv")