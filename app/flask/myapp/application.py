'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request
from application import db
from application.models import Data
from application.forms import EnterDBInfo, RetrieveDBInfo
from application.visual import plot

#from flask_bootstrap import Bootstrap

# Elastic Beanstalk initalization
application = Flask(__name__)
#Bootstrap(application)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'   

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    form1 = EnterDBInfo(request.form) 
    form2 = RetrieveDBInfo(request.form) 
    
    
    # if request.method == 'POST' and form1.validate():
    #     data_entered = Data(notes=form1.dbNotes.data)
    #     try:     
    #         db.session.add(data_entered)
    #         db.session.commit()        
    #         db.session.close()
    #     except:
    #         db.session.rollback()
    #     return render_template('thanks.html', notes=form1.dbNotes.data)
        
    # if request.method == 'POST' and form2.validate():
    #     try:   
    #         num_return = int(form2.numRetrieve.data)
    #         query_db = Data.query.order_by(Data.id.desc()).limit(num_return)
    #         for q in query_db:
    #             print(q.notes)
    #         db.session.close()
    #     except:
    #         db.session.rollback()
    #     return render_template('results.html', results=query_db, num_return=num_return)                
    
    #return render_template('index.html', form1=form1, form2=form2)
    return render_template('index.html')

@application.route('/visualization', methods=['GET', 'POST'])
def visualization():
    desc = "The historical data of the region is displayed below."
    if request.method == 'POST':
        input_zip = my_form_post()
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

def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@application.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('prediction.html')

#@application.route('/visualization', methods=['POST'])


if __name__ == '__main__':
    application.run(host='0.0.0.0')
