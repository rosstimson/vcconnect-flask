from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Required
from .vcconnect import get_main_area_dropdown

class MainAreaForm(FlaskForm):
    choices = get_main_area_dropdown()
    area = SelectField('Main Area', coerce=int, choices=choices, validators=[Required()])
    submit = SubmitField('Submit')
