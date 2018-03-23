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



def get_diff_mean(allzips,zipcode,df,allhome):
     # subset 3 years
     df = pd.concat([DataFrame(df['RegionName']),df[df.columns[-36:]]],axis =1)
     # subset those appear in base price data
     df = df[df['RegionName'].isin(allzips)]
     # get mean price difference for the region
     allhome_price = allhome.loc[allhome['RegionName'] == zipcode].drop(['RegionName'],axis=1)
     if (allhome_price.shape[0]==0):
          return(np.nan)
     else:
          df_price = df.loc[df['RegionName'] == zipcode].drop(['RegionName'],axis=1)
          diff = (df_price.values - allhome_price.values)*1.0/allhome_price.values
          return(diff.mean())



if __name__ == '__main__':
     # get all zipcodes available in base price data
     price = pd.read_csv('newdata/Zip_MedianListingPrice_AllHomes.csv',converters={'RegionName': str})
     allzips = price['RegionName'].values

     # read all home type data
     allhome = pd.read_csv('newdata/Zip_Zhvi_AllHomes.csv',converters={'RegionName': str})
     bed1 = pd.read_csv('newdata/Zip_Zhvi_1bedroom.csv',converters={'RegionName': str})
     bed2 = pd.read_csv('newdata/Zip_Zhvi_2bedroom.csv',converters={'RegionName': str})
     bed3 = pd.read_csv('newdata/Zip_Zhvi_3bedroom.csv',converters={'RegionName': str})
     bed4 = pd.read_csv('newdata/Zip_Zhvi_4bedroom.csv',converters={'RegionName': str})
     bed5 = pd.read_csv('newdata/Zip_Zhvi_5bedroomOrMore.csv',converters={'RegionName': str})
     single = pd.read_csv('newdata/Zip_Zhvi_SingleFamilyResidence.csv',converters={'RegionName': str})
     condo = pd.read_csv('newdata/Zip_Zhvi_Condominum.csv',converters={'RegionName': str})

     # subset 3 years
     allhome = pd.concat([DataFrame(allhome['RegionName']),allhome[allhome.columns[-36:]]],axis =1)

     # subset those appear in base price data
     allhome = allhome[allhome['RegionName'].isin(allzips)]

     # get mean of difference for all regions
     all_means = [[]]
     for i in range(len(allzips)):
          zipcode = allzips[i]
          bed1_mean = get_diff_mean(allzips,zipcode,bed1,allhome)
          bed2_mean = get_diff_mean(allzips,zipcode,bed2,allhome)
          bed3_mean = get_diff_mean(allzips,zipcode,bed3,allhome)
          bed4_mean = get_diff_mean(allzips,zipcode,bed4,allhome)
          bed5_mean = get_diff_mean(allzips,zipcode,bed5,allhome)
          single_mean = get_diff_mean(allzips,zipcode,single,allhome)
          condo_mean = get_diff_mean(allzips,zipcode,condo,allhome)
          means = [zipcode,bed1_mean,bed2_mean,bed3_mean,bed4_mean,bed5_mean,single_mean,condo_mean,]
          all_means.append(means)
          if (i % 100 ==0):
               print(i)
     all_means =  all_means[1:len(all_means)]
     all_means= DataFrame(all_means,columns=["zipcode","bed1","bed2","bed3","bed4","bed5","single","condo"])    
     all_means.to_csv("adjust_means.csv")









