'''
Flask application to predict housing price

Deployed to Amazon Web Services using Elastic Beanstalk and RDS
'''

from flask import Flask, render_template, request
from application import db
from application.models import Data
from application.forms import EnterDBInfo, RetrieveDBInfo
from application.visual import plot
from application.prediction import predict_price, all_parameters, all_means
# Pandas
import pandas as pd
import numpy as np

#from flask_bootstrap import Bootstrap

# Elastic Beanstalk initalization
application = Flask(__name__)
#Bootstrap(application)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'

# try:
#     df1.to_sql("df1", db.engine)
#     print("New df1 generated")
# except:
#     print("filled")

# data = pd.read_sql('SELECT * FROM df1', db.engine)
# print(data)

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    # form1 = EnterDBInfo(request.form) 
    # form2 = RetrieveDBInfo(request.form) 
    # if request.method == 'POST' and form1.validate():
    #     data_entered = Data(notes=form1.dbNotes.data)
    #     try:     
    #         db.session.add(data_entered)
    #         db.session.commit()        
    #         db.session.close()
    #     except:
    #         db.session.rollback()
    #     return render_template('thanks.html', notes=form1.dbNotes.data)
    return render_template('index.html')

@application.route('/visualization', methods=['GET', 'POST'])
def visualization():
    desc = "The historical data of the region is displayed below."
    if request.method == 'POST':
        input_zip = request.form['zipcode']
        if (plot(input_zip)=="error"):
            [x,y1,y2,miss] = plot("60201")
            desc = "The input zip code is invalid."
        else:
            [x,y1,y2,miss] = plot(input_zip)
            #location = detect_loc(input_zip)         
    else:
        [x,y1,y2,miss] = plot("60201")
        #location = detect_loc("60201")
    return render_template('visualization.html', labels = x, data = y1, data2 = y2, data3 = miss, result_desc = desc)

@application.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # ??? please know how to test the validity of those things!
        zipcode = request.form['zipcode']
        # YYYY-MM, e.g. 2018-10
        date = request.form['date']
        # e.g. bed2
        hometype = request.form['hometype']
        price = predict_price(zipcode, date, hometype, all_parameters, all_means)
        print(price)
    return render_template('prediction.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0')
