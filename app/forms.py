from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    IntegerField,
    BooleanField
)
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class CounterForm(FlaskForm):
    player_1 = StringField('Player 1', validators=[DataRequired()])
    player_2 = StringField('Player 2', validators=[DataRequired()])

    score_1 = IntegerField('Score 1', validators=[DataRequired()])
    score_2 = IntegerField('Score 2', validators=[DataRequired()])

    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')