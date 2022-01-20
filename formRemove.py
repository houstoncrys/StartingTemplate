from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RemoveForm(FlaskForm):
  remove = StringField('What item(s) did you complete?')
  removeSubmit = SubmitField('Remove')
  back = SubmitField('Back')