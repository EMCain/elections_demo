from flask import Flask, render_template, url_for
from app import app 

@app.route('/')
def hello_world():
    return render_template('base.html', content='page content here', title='Example Page')