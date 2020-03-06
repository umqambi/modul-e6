from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class NumFiboForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    submit = SubmitField('Calculate')
