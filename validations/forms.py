from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField,SelectField)
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    nis =  IntegerField(label='NIS',validators=[InputRequired(),Length(max=5)])
    name = StringField(label='Name',validators=[InputRequired(),Length(max=200)])
    number_absence = IntegerField(label='Number Absence',validators=[InputRequired(),Length(2)])
    major = SelectField(label='Major',choices=['SIJA', 'DKV', 'MM', 'TKJ', 'TITL', 'TAV', 'TKR', 'TP', 'KGSP', 'GEOMATIKA'],default='SIJA',validators=[InputRequired()])
    year_graduated = IntegerField(label='Year Graduated',validators=[InputRequired(),Length(max=4)])