# This test file provides unit tests for functions in prediction.py 
from datetime import datetime
from prediction import diff_month, check_date, timeseries_predict, adjust_predict, predict_price
from collections import OrderedDict
import pandas as pd

# test diff_month()
def test_diff_month():
     d1 = datetime.strptime('2017-12', '%Y-%m')
     d2 = datetime.strptime('2016-06', '%Y-%m')
     expected = 18
     assert  diff_month(d1,d2) == expected

# test check_date()
def test_check_date():
     test_date = '2018-04'
     expected = True
     assert check_date(test_date) == expected
                      
# test timeseries_predict()
def test_timeseries_predict():
     df = {'zipcode': ['10025', '60201'], 'residual_median': [100, 200],
           'residual_sd':[40000,10000], 'intercept':[1500000,500000],
          'slope':[1300,1000],'c1':[12,6],'c2':[11,5],'c3':[10,4],
          'c4':[9,3],'c5':[8,2],'c6':[7,1],'c7':[7,1],'c8':[8,2],
          'c9':[9,3],'c10':[10,4],'c11':[11,5],'c12':[12,6]}
     all_parameters = pd.DataFrame(OrderedDict(df))
     zipcode = '10025'
     test_date = '2018-12'
     expected = ['10025',1546909,40000]
     result = timeseries_predict(all_parameters,zipcode,test_date)
     assert [x.values[0] for x in result] == expected


# test adjust_predict()
def test_adjust_predict():
     df = {'zipcode': ['10025', '60201'], 'residual_median': [100, 200],
           'residual_sd':[40000,10000], 'intercept':[1500000,500000],
          'slope':[1300,1000],'c1':[12,6],'c2':[11,5],'c3':[10,4],
          'c4':[9,3],'c5':[8,2],'c6':[7,1],'c7':[7,1],'c8':[8,2],
          'c9':[9,3],'c10':[10,4],'c11':[11,5],'c12':[12,6]}
     all_parameters = pd.DataFrame(OrderedDict(df))
     base_result = timeseries_predict(all_parameters,'10025','2018-12')
     zipcode = 10025
     hometype = 'bed2'
     df_means = {'zipcode': ['10025'], 'bed1':[-0.2],'bed2':[-0.1],'bed3':[0],
                 'bed4':[0.5],'bed5':[1],'single':[1.5],'condo':[0]}
     all_means = pd.DataFrame(OrderedDict(df_means))
     all_means = pd.read_csv("static/data/prediction/adjust_means.csv")
     result = adjust_predict(all_means, base_result, hometype, zipcode)
     expected = [1916860.544750242, 1838460.544750242, 1995260.544750242]
     assert expected == result
     
# test predict_price()
def test_predict_price():
     zipcode = '10025'
     test_date = '2018-12'
     hometype = 'bed2' 
     df = {'zipcode': ['10025', '60201'], 'residual_median': [100, 200],
           'residual_sd':[40000,10000], 'intercept':[1500000,500000],
          'slope':[1300,1000],'c1':[12,6],'c2':[11,5],'c3':[10,4],
          'c4':[9,3],'c5':[8,2],'c6':[7,1],'c7':[7,1],'c8':[8,2],
          'c9':[9,3],'c10':[10,4],'c11':[11,5],'c12':[12,6]}
     all_parameters = pd.DataFrame(OrderedDict(df))
     df_means = {'zipcode': ['10025'], 'bed1':[-0.2],'bed2':[-0.1],'bed3':[0],
                 'bed4':[0.5],'bed5':[1],'single':[1.5],'condo':[0]}
     all_means = pd.DataFrame(OrderedDict(df_means))
     result = predict_price(zipcode, test_date, hometype, all_parameters, all_means)
     expected = [1392218.1000000001, 1313818.1000000001, 1470618.1000000001]
     assert expected == result
     
     
     





