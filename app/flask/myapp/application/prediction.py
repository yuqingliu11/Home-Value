import pandas as pd
import numpy as np
# from statsmodels.tsa.seasonal import seasonal_decompose
from pandas import Series,DataFrame,DatetimeIndex
from scipy import stats
from datetime import datetime

# compute difference of dates in number of months
def diff_month(d1, d2):
   """Takes in two month and return the number of difference between two dates."""
   diff = (d1.year - d2.year) * 12 + d1.month - d2.month
   return(diff)

# check if user input date is valid
def check_date(test_date):
   """Takes a date and check if the date matches yyyy-mm format and between 2018-01 and 2099-12."""
   if (len(test_date.split('-'))==2):
          date = test_date.split('-')
          try:
               if (int(date[0])>2017 and int(date[0])<2100 and int(date[1])>0 and int(date[1])<13):
                    return(True)
               else:
                    return(False)
          except ValueError:
               return False
   else:
          return(False)
     

# predict median price of a region with time series components
def timeseries_predict(all_parameters, zipcode,test_date):
   """This function provides a initial prediction for the given zip code and test date.
	It first test the input zipcode is valid, then pull out the time series decomposition
	parameters from the database and utilize the parameters to predict the future date
	home value.

	Args:
		all_parameters: pre saved csv in the directory that contains the time series
						decompositon parameters and mean/sd of random noise for all zip codes.
		zipcode: user input zip code string.
		test_date: user input date in yyyy-mm format.

	Returns:
		A list of three element: user input zip code, point estimation, standard deviation of
		random noise component.

	"""
   zip_parameters = all_parameters.loc[all_parameters['zipcode'] == zipcode]
   if (zip_parameters.shape[0] == 0):
          return("The input zipcode is not available.")
   else:
          test_noise = zip_parameters["residual_median"]
          gap = diff_month(datetime.strptime(test_date, '%Y-%m'),datetime.strptime('2017-12', '%Y-%m'))
          test_trend = zip_parameters["intercept"] + zip_parameters["slope"] * (24+gap)
          test_season = zip_parameters.values[0][-12:][gap%12-1]
          test_pred = test_noise + test_trend + test_season
          return([zip_parameters["zipcode"]]+[test_pred]+[zip_parameters["residual_sd"]])

# predict median price of different home types in the region
def adjust_predict(all_means, base_result, hometype, zipcode):
   """This function improves the prediction from timeseries_predict() with home type means.

	Args: 
		all_means: pre saved csv contains median home value of seven home types for all zipcodes.
		base_result: a list contains initial prediction by timeseries_predict().
		hometype: user input a string indicating the interest home type; 7 categories allowed.
		zipcode: user input zip code string.

	Returns:
		A list of three elements: adjusted point estimation, lower bound of 95% CI,
		higher bound of 95% CI.

   """
   means = all_means.loc[all_means['zipcode'] == zipcode]
   if (np.isnan(means[hometype].values[0])):
          result = base_result[1]*(1+all_means[hometype].median())
   else:          
          result = base_result[1]*(1+means[hometype]).values[0]
   upper = result + 1.96*base_result[2]
   lower = result - 1.96*base_result[2]
   return([result.values[0],lower.values[0],upper.values[0]])

# combine the two functions above
def predict_price(zipcode, test_date, hometype, all_parameters, all_means):
   """This function combines timeseries_predict() and adjust_predict(). It checks the
	validity of user input date first, then call timeseries_predict() and adjust_predict()
	to output prediction results or error message."""
   if (check_date(test_date)):
        base_result = timeseries_predict(all_parameters, zipcode, test_date)
        if (type(base_result)!=str):
               final_result = adjust_predict(all_means, base_result, hometype, zipcode)
               return(final_result)
        else:
               return(base_result)
   else:
          return("The input date is invalid.")

