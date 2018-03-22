'''
Flask application to predict housing price

Deployed to Amazon Web Services using Elastic Beanstalk and RDS
'''
from flask import Flask, render_template, request
from application import db
from application.visual import plot
from application.prediction import predict_price

# Pandas
import pandas as pd
import numpy as np
# from flask_bootstrap import Bootstrap

# Elastic Beanstalk initalization
application = Flask(__name__)
# Bootstrap(application)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'
# application.secret_key = 'yfvjkI7803otyFhkmgvv'

try:
    all_parameters = pd.read_sql('SELECT * FROM all_parameters', db.engine)
    all_means = pd.read_sql('SELECT * FROM all_means', db.engine)
    # print("all_parameters:")
    # print(all_parameters)
    # print("all_means:")
    # print(all_means)
    print("Modeling data loaded from SQL successfully.")
except:
    print("Failed to retrieve modeling data from SQL.")

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@application.route('/visualization', methods=['GET', 'POST'])
def visualization():
    #input_zip = "60201"
    if request.method == 'POST':
        input_zip = request.form['zipcode']
        if (plot(input_zip)=="error"):
            [x,y1,y2,miss] = plot("60201")
            desc = "The input zip code is invalid."
        else:
            [x,y1,y2,miss] = plot(input_zip)
            desc = "The historical data of zip code " + input_zip + " is displayed below."
            #location = detect_loc(input_zip)         
    else:
        [x,y1,y2,miss] = plot("60201")
        desc = "The historical data of zip code 60201 is displayed below."
        #location = detect_loc("60201")
    #desc = "The historical data of zip code " + input_zip + " is displayed below."
    return render_template('visualization.html', labels = x, data = y1, data2 = y2, data3 = miss, result_desc = desc)

@application.route('/prediction', methods=['GET', 'POST'])
def prediction():
    output = "    "
    if request.method == 'POST':
        # ??? please know how to test the validity of those things!
        zipcode = request.form['zipcode']
        # YYYY-MM, e.g. 2018-10
        date = request.form['date']
        # e.g. bed2
        hometype = request.form['type']

        pred = predict_price(zipcode, date, hometype, all_parameters, all_means)

        if (type(pred)==str):
            output = pred
        else:
            pred = [int(p) for p in pred]
            output = "The estimated price is between $"+ str(pred[1]) +" and $" + str(pred[2]) + "."
    
    return render_template('prediction.html', prediction = output)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
