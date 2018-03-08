import pandas as pd
import numpy as np

def plot(zipcode):
     price = pd.read_csv('static/data/Zip_MedianListingPrice_AllHomes.csv',converters={'RegionName': str})
     sqft = pd.read_csv('static/data/Zip_MedianListingPricePerSqft_AllHomes.csv',converters={'RegionName': str})
     searched_zip = price.loc[price['RegionName'] == zipcode]
     if (searched_zip.shape[0]==0):
          return("error")
     else:
          dates = price.columns[len(price.columns)-12*5-1 : len(price.columns)]
          x = range(len(price.columns)-12*5-1,len(price.columns))
          yprice = (price.loc[price['RegionName']==zipcode,dates]).values/1000
          missing = np.isnan(yprice).sum() 
          yprice = yprice.reshape(61,1).tolist()
          yprice = [item for sublist in yprice for item in sublist]
          missing_fill = [yprice[missing]]*(missing+1) + [np.nan]*(61-missing-1)
          price_period = price.iloc[:,len(price.columns)-12*5-1 : len(price.columns)]
          national_mean = price_period.mean(axis=0)/1000
          national_mean = national_mean.tolist()
          return(x, yprice, national_mean, missing_fill)

#def detect_loc(zipcode):  
#	 price = pd.read_csv('static/data/Zip_MedianListingPrice_AllHomes.csv',converters={'RegionName': str})
#     searched_zip = price.loc[price['RegionName'] == zipcode]
#     location = (', ').join(searched_zip[['City','State']] .values.tolist()[0])
     return(location)  

def plot_state():   
     state = "CA"
     x = range(len(price.columns)-12*5-1,len(price.columns))
     dates = price.columns[len(price.columns)-12*5-1 : len(price.columns)]
     searched_state = price.loc[price['State'] == state, dates]
     state_mean = searched_state.mean(axis=0)
     return(x,state_mean)




