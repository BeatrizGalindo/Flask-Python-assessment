from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Write here your user name:')
    email_address = StringField(label='Write here your email:')
    password_hash = PasswordField(label='Password:')
    password_hash_confirm = PasswordField(label='Confirm your password:')
    submit = SubmitField(label='submit')
