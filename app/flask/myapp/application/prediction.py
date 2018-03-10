import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas import Series,DataFrame,DatetimeIndex
from scipy import stats
from datetime import datetime
# import datetime
# from statsmodels.tsa.arima_model import ARIMA
# from pandas.tools.plotting import autocorrelation_plot
# import statistics
# import matplotlib.pyplot as plt

# compute difference of dates in number of months
def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

# predict median price of a region with time series components
def timeseries_predict(all_parameters, zipcode,test_date):
     zip_parameters = all_parameters.loc[all_parameters['zipcode'] == zipcode]
     if (zip_parameters.shape[0] == 0):
          return("zipcode not found")
     else:
          test_noise = zip_parameters["residual_median"]
          gap = diff_month(datetime.strptime(test_date, '%Y-%m'),datetime.strptime('2017-12', '%Y-%m'))
          test_trend = zip_parameters["intercept"] + zip_parameters["slope"] * (24+gap)
          test_season = zip_parameters.values[0][-12:][gap%12-1]
          test_pred = test_noise + test_trend + test_season
          return([zip_parameters["zipcode"]]+[test_pred]+[zip_parameters["residual_sd"]])

# predict median price of different home types in the region
def adjust_predict(all_means, base_result,hometype, zipcode):
     means = all_means.loc[all_means['zipcode'] == zipcode]
     if (np.isnan(means[hometype].values[0])):
          result = base_result[1]*(1+all_means[hometype].median())
     else:          
          result = base_result[1]*(1+means[hometype]).values[0]
     upper = result + 1.96*base_result[2]
     lower = result - 1.96*base_result[2]
     return([result.values[0],lower.values[0],upper.values[0]])

# combine the two functions above
def predict_price(zipcode,test_date,hometype,all_parameters,all_means):
     base_result = timeseries_predict(all_parameters, zipcode, test_date)
     if (type(base_result)!=str):
          final_result = adjust_predict(all_means, base_result,hometype,zipcode)
          return(final_result)
     else:
          return(base_result)

