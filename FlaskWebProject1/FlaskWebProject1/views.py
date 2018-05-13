"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from FlaskWebProject1 import app
from flask import json
from nameparser import HumanName

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about/',methods=('get', 'post'))
def about():
    full=request.args.get("full")
    result=[]
    a=parseNames(full);
    empDict = {
        'Last':a.last,
        'First':a.first,
        'Middle': a.middle,
        'Suffix': a.suffix}
    result.append(empDict)
    return json.dumps(result)



def parseNames(fullname):
    return HumanName(fullname)
