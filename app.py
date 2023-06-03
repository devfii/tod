from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return 'app is running'

@app.route('/date')
def get_date():
    today = datetime.today().strftime("%A, %d %B %Y")
    return today

