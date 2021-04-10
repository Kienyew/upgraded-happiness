from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from .models import User

EMAIL_VALIDATORS = [DataRequired(), Email()]
PASSWORD_VALIDATORS = [DataRequired(), Length(8, 64)]
USERNAME_VALIDATORS = [DataRequired(), Length(
    4, 64), Regexp('^[a-zA-Z0-9_]+$', message='Username can contains only latin characters and digits')]


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=EMAIL_VALIDATORS)
    username = StringField('Username', validators=USERNAME_VALIDATORS)
    password = PasswordField('Password', validators=PASSWORD_VALIDATORS)
    password_confirm = PasswordField(
        'Confirm password', validators=PASSWORD_VALIDATORS + [EqualTo('password', "Password doesn't match!")])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already taken')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken')


class LoginForm(FlaskForm):
    email_or_username = StringField('Email or username')
    password = PasswordField('Password', validators=PASSWORD_VALIDATORS)
    submit = SubmitField('Log in')
