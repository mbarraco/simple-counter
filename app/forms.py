from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    IntegerField
)
from wtforms.validators import DataRequired

class CounterForm(FlaskForm):
    player_1 = StringField('Player 1', validators=[DataRequired()])
    player_2 = StringField('Player 2', validators=[DataRequired()])

    score_1 = IntegerField('Score 1', validators=[DataRequired()])
    score_2 = IntegerField('Score 2', validators=[DataRequired()])

    submit = SubmitField('Sign In')