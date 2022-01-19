from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):
    toDo = StringField('What would you like to do?')
    addSubmit = SubmitField('Add')

# class RemoveForm(FlaskForm):
#     remove = StringField('What item(s) did you complete?')
#     removeSubmit = SubmitField('Remove')