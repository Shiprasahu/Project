

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=8, max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    #confirmpassword = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    name = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired()])
    #lastname = StringField('Lastname', validators=[DataRequired()])
    #phonenumber = IntegerField('Phonenumber', validators=[DataRequired()])
    submit = SubmitField('Register')