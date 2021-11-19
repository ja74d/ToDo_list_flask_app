#!/usr/bin/python3

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'mysecretkey'

class Tasks(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Task('{self.task}')"

@app.route('/', methods=['GET', 'POST'])
def index():
    task = None
    form = Tasks()
    if form.validate_on_submit():
        task = Task(task=form.task.data)
        db.session.add(task)
        db.session.commit()
        form.task.data = ''
    tasks = Task.query.all()  
    return render_template('index.html', form=form, tasks=tasks)