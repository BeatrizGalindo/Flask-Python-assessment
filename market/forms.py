from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField(label='Write here your user name:', validators=[DataRequired(),Length(min=3, max=10)])
    email_address = StringField(label='Write here your email:', validators=[DataRequired(),Email()])
    password_hash = PasswordField(label='Password:', validators=[DataRequired(),Length(min=5)])
    password_hash_confirm = PasswordField(label='Confirm your password:', validators=[DataRequired(),EqualTo('password_hash')])
    submit = SubmitField(label='Submit')
