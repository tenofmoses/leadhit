from pymongo import MongoClient
client = MongoClient(host='mongo')

db = client.app
forms = db.forms
db.forms.remove({})

list_forms = [{"name": "Form login", "login_email":"email", "login_password":"text"},
            {"name": "Form registration", "reg_login":"text", "reg_email":"email", "reg_phone":"phone", "reg_password":"text"},
            {"name": "Form feedback", "feedback_email":"email", "feedback_text":"text", "feedback_date":"date"},]

forms.insert_many(list_forms)
