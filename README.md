# Music-Recommender
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/johnnychiuchiu/Machine-Learning/blob/master/LICENSE)

* **Vision**: Engage music fans by recommending select number of songs based on user’s song and genre preference.
* **Mission**: The goal of the project is to help people discover the music they may enjoy by providing them a list of recommended songs according to their favorite musicians and songs. This will be done using a collaborative filtering or a latent factor recommender model that is trained with the [Million Song Dataset](https://www.google.com/search?q=million+song+dataset&oq=million+so&aqs=chrome.0.69i59j69i60l2j69i61j69i57j0.5455j0j7&sourceid=chrome&ie=UTF-8).
* **SuccessCriteria**: Successfully deployed a web application that dynamically shows a recommended list of songs according to users’ input.

For this project, we used Pivotal Tracker, an Agile Project Management Software, to keep track of the overall progress. The pivotal tracker page for this project can be reached by clicking on [this link](https://www.pivotaltracker.com/n/projects/2142509).

Suggested steps to deploy app
------------

1. Clone repository.
2. Create virtual environment

   ```
   > HomeValue$ source flask-aws/bin/activate
   ```
3. Install required packages

   ```
   > HomeValue$ pip install -r requirements.txt
   ```
  
4. Set up music.env file with the following structure
   
   ```
   export DATABASE_URL=XXX
   export HOST=XXX    
   export USER=XXX
   export PASSWORD=XXX
   export DBNAME=XXX    
   export PORT=XXX
   ```

5. Set environment variables from file

   ```
   source music.env
   ```

6. (OPTIONAL) If you want to run unit tests before running the code, run the following commands:

   ```
   > (musicproject) Music-Recommender$ py.test
   ```

7. Get data and save it into your mySQL database

   ```
   > (musicproject) Music-Recommender$ cd src/database   
   > (musicproject) database$ python create_db.py  
   > (musicproject) database$ python insert_data.py
   ```


   Note that the data is downloaded from the url provided by the company [Turi](https://turi.com/) using the following two hyperlinks. [Download User Listening History Data](https://static.turi.com/datasets/millionsong/10000.txt) and [Download Song Meta Data](https://static.turi.com/datasets/millionsong/song_data.csv).

8. Launch the application

   ```
   > (musicproject) Music-Recommender$ python application.py
   ```


   

Application Screenshot
------------

![](https://github.com/johnnychiuchiu/Music-Recommender/blob/refactor/directory/pic/page2.png)


Documentation
------------
* `modelSelectionAndTuning.ipynb`: Jupyter Notebook that contains a walkthrough of the overall model building, model selection and parameter tuning. [[jupyter notebook](https://github.com/johnnychiuchiu/Music-Recommender/blob/refactor/directory/src/notebooks/modelSelectionAndTuning.ipynb)]

* `latentFactorModel.ipynb`: An old version of the overall model building process. [[jupyter notebook](https://github.com/johnnychiuchiu/Music-Recommender/blob/sprint_1/develop/notebooks/latentFactorModel.ipynb)]

* Step by step guide for database, environment and sphinx documentation set up. [[Github Wiki](https://github.com/johnnychiuchiu/Music-Recommender/wiki)]

* You can find the slides for this project [here](https://github.com/johnnychiuchiu/Music-Recommender/blob/final-sprint/Music%20Recommender.pdf).

Project Organization
------------

    ├── LICENSE
    │
    ├── README.md          <- The top-level README for developers using this project.
    │    
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`               
    │
    ├── pic                <- some picture for demo purpose
    │
    ├── web                <- HTML and CSS files
    │    
    ├── form               <- user form selection files
    │   
    ├── data               <- Data files
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── database       <- Scripts to download and generate data
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make predictions
    │   │
    │   └── notebooks      <- Jupyter notebooks. Used to reate exploratory, results oriented visualizations,  and parameter tuning                     
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details





