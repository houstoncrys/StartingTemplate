from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):
    toDo = StringField('What would you like to do?')
    addSubmit = SubmitField('Add')
    removeSubmit = SubmitField('Remove')