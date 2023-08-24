from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email_address')
    password_hash = PasswordField(label='password_hash')
    password_hash_confirm = PasswordField(label='password_hash_confirm')
    submit = SubmitField(label='submit')
