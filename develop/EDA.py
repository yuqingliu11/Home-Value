import pandas as pd
import numpy as np
from numpy import array
from sqlalchemy import create_engine
import plotly.plotly as py
import matplotlib.pyplot as plt


engine = create_engine('postgresql://cc:ccdabian@localhost/home_value_db')
price = pd.read_sql_query('SELECT * FROM "City_MedianListingPrice"', engine)
price.shape


# need user input on the web app
city ='San Jose'

dates = price.columns[len(price.columns)-12*5-1 : len(price.columns)]
x = range(len(price.columns)-12*5-1,len(price.columns))
y = (price.loc[price['RegionName']==city,dates]).values
y =y.reshape(61,1).tolist()
my_xticks = ['2012','2013','2014','2015','2016','2017']
plt.xticks([41,53,65,77,89,101], my_xticks)
plt.plot(x,y)
