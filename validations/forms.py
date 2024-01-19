from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, FileField
from wtforms.validators import InputRequired, Length, NumberRange

class RegisterForm(FlaskForm):
    nis = IntegerField(label='NIS', validators=[InputRequired(), NumberRange(min=1, max=99999)])
    name = StringField(label='Name', validators=[InputRequired(), Length(max=200)])
    number_absence = IntegerField(label='Number Absence', validators=[InputRequired(), NumberRange(min=0, max=99)])
    major = SelectField(
        label='Major',
        choices=[('SIJA', 'SIJA'), ('DKV', 'DKV'), ('MM', 'MM'), ('TKJ', 'TKJ'),
                 ('TITL', 'TITL'), ('TAV', 'TAV'), ('TKR', 'TKR'), ('TP', 'TP'),
                 ('KGSP', 'KGSP'), ('GEOMATIKA', 'GEOMATIKA')],
        default='SIJA',
        validators=[InputRequired()]
    )
    year_graduated = IntegerField(label='Year Graduated', validators=[InputRequired(), NumberRange(min=1900, max=2100)])
    photo = FileField(label='Photo', validators=[InputRequired()])
