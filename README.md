# Home Value Prediction

* **Vision**: This project aims to provide a tool to inform home values to the users who are buying or selling a property. Real Estate is usually an important decision and large expense for most households, and people always conducted careful research about their needs and cost to decide when, where and what to buy. Zillow, an online real estate database company, has released detailed information of the home values in United States for the past 20 years, including median price, location, home type, built year, etc.
* **Mission**: Build a time series model to predict the home value in the future using the data provided by Zillow, which has released detailed information of the home values in United States for the past 20 years. A web app will be deployed with the model integrated and allow users to input location/zip code, type, and time of purchase to get an estimation for the home value and also display the historical trend of home values based on user’s input.[Zillow Dataset](https://www.zillow.com/research/data/).
* **SuccessCriteria**: Successfully deployed a web application that can display visualization for historical data and make predictios for future home values.


To reproduce the application
------------

1. Clone repository. 

2. Enter virtual environment under HomeValue/app

   ```
   > HomeValue$ source flask-aws/bin/activate
   ```

3. Go to HomeValue/app/application and install required packages 

   ```
   > HomeValue$ pip install -r requirements.txt
   ```
  
4. (optional and not suggested) Regenerate parameter files(already included in HomeValue/app/application/static/data/prediction). 

   ```
   > HomeValue$ python base_timeseries.py
   > HomeValue$ python type_adjustment.py
   ```

5. Run application

   ```
   > HomeValue$ cd myapp
   > HomeValue$ python application.py
   ```
   

Application Screenshot
------------

[Home](https://github.com/yuqingliu11/Home-Value/Home.png)
[Visualization](https://github.com/yuqingliu11/Home-Value/Visual.png)
[Prediction](https://github.com/yuqingliu11/Home-Value/Prediction.png)


Repository Structure
------------

    ├── LICENSE
    │
    ├── README.md                 <- Decription of how to reproduce the application.
    │    
    ├── requirements.txt          <- The requirements file with python package names to reproduce the. environment.
    │
    ├── analyze                   <- Data exploration process.
    │    
    ├── doc                       <- Sphinx documention files.
    │   
    ├── screenshots               <- Screen shots of the web applicatio interface.
    │
    ├── app                       <- Source code for the project.
    │   │
    │   ├── flask-aws             <- Virtual Enviornment.
    │   │
    │   ├── myapp                 <- All files for running the application.
    │         │
    │         ├── application     <- backend algorithms.
    │         │       │ 
    │         │       ├── base_timeseries.py     <- Generate parameter file "base_parameters.csv"
    │         │       │ 
    │         │       ├── type_adjustment.py     <- Generate parameter file "adjust_means.csv"
    │         │       │ 
    │         │       ├── visual.py              <- Script to visualize user input data on 'Visualization' page of the web
    │         │       │ 
    │         │       ├── prediction.py          <- Script to make predictions on 'Prediction' page of the web
    │         │       │ 
    │         │       ├── unittest.py            <- Unit test script for functions in prediction.py
    │         │             
    │         ├── static          <- Data, images and style files for front end.
    │         │             
    │         ├── templates       <- Html files for user interface.


Other
------------

Team:
  Developer: Yuqing Liu
  Project Owner: Johnny Chiu
  QA: Spencer Moon

[Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2143068) helped the team track project progress.

The presentation slides can be found [here](https://github.com/yuqingliu11/Home-Value/Demo.pdf)

  


