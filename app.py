#!/usr/bin/python3

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

app.secret_key = 'mysecretkey'

#tasks form
class Tasks:
    task = db.Column(db.String(255), nullable=False)
    submit = SubmitField('Add')


@app.route('/')
def index():
    return render_template('index.html')