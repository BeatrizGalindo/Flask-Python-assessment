from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from market.models import User
class RegisterForm(FlaskForm):

    # Validating that we don't repeat users in the database
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already exist')


    username = StringField(label='Write here your user name:', validators=[DataRequired(),Length(min=3, max=10)])
    email_address = StringField(label='Write here your email:', validators=[DataRequired(),Email()])
    password_hash = PasswordField(label='Password:', validators=[DataRequired(),Length(min=5)])
    password_hash_confirm = PasswordField(label='Confirm your password:', validators=[DataRequired(),EqualTo('password_hash')])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label='Write here your user name:', validators=[DataRequired(),Length(min=3, max=10)])
    password_hash = PasswordField(label='Password:', validators=[DataRequired(),Length(min=5)])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')
class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')
class AddItemForm(FlaskForm):
    submit = SubmitField(label='Add Item')