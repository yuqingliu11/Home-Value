from application import db
import pandas as pd

def clear_data(db):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print 'Clear table %s' % table
        db.session.execute(table.delete())
    db.session.commit()

# We don't really have any predefined table to creat
# aka: No class Data(db.Model):
# db.create_all()

db.drop_all()
drop_all_means = 'DROP TABLE IF EXISTS all_means;'
drop_all_parameters = 'DROP TABLE IF EXISTS all_parameters'
db.session.execute(drop_all_means)
db.session.execute(drop_all_parameters)
csv_parameters = pd.read_csv('static/data/prediction/base_parameters.csv',converters={'zipcode': str})
csv_means = pd.read_csv('static/data/prediction/adjust_means.csv',converters={'zipcode': str})
# print("csv_parameters")
# print(csv_parameters)
# print("csv_means")
# print(csv_means)
print("Original CSV data loaded.")

try:
    csv_parameters.to_sql("all_parameters", db.engine, index = False)
    print("Added all_parameters table to SQL.")
except:
    print("Skipped table initialization. all_parameters table already exists.")
try:
    csv_means.to_sql("all_means", db.engine, index = False)
    print("Added all_means table to SQL.")
except:
    print("Skipped table initialization. all_means table already exists.")

print("Parameters and Intermediate Data Successfully Loaded in SQL...")
