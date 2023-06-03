from flask import Flask
from datetime import datetime
app = Flask(__name__)

'''
Function to check if app is running
'''
@app.route('/')
def home():
    return 'app is running'

'''
Function to check current date and version of app running
'''
@app.route('/date')
def get_date():
    today = datetime.today().strftime("%A, %d %B %Y")
    return today

