from flask import Flask, request
from flask_pymongo import PyMongo
import re
import json

app = Flask(__name__)
app.config['MONGO_HOST'] = 'mongo'
mongo = PyMongo(app)

def is_date(date):
    if re.match(r'^\d{2}\.\d{2}\.\d{4}$', date):
        return True
    if re.match(r'^\d{4}\-\d{2}\-\d{2}$', date):
        return True
    return False

def is_phone(phone):
    if re.match(r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', phone):
        return True
    return False

def is_email(email):
    if re.match(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', email):
        return True
    return False

def get_type(value):
    if is_date(value):
        return 'date'
    if is_phone(value):
        return 'phone'
    if is_email(value):
        return 'email'
    return 'text'

def get_form(data):
    data_fields = {}
    for key, value in data.items():
        data_type = get_type(value)
        data_fields[key] = data_type
    return data_fields


@app.route('/get_form', methods=['POST'])
def page():
    data = request.form
    form = mongo.db.forms.find_one(get_form(data))
    if not form:
        return json.dumps(get_form(data))
    return form['name']


if __name__ == '__main__':
    app.run(host='0.0.0.0')
