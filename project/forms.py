from enum import unique
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms import StringField, PasswordField, HiddenField

class RegisterForm(FlaskForm):
    """로그인 등록 폼

    Args:
        FlaskForm (_class_): flaskform
    """
    userId = StringField('userId', id='userId', validaotors=[DataRequired(), Length(min=5, max=12)])
    password = PasswordField('password', id='password', validators=[DataRequired(), Length(min=7, max=20)])
    confirmPassword = PasswordField('confirmPassword', id='confirmPassword', validators=[DataRequired(), EqualTo('password')])
    email = StringField('email', id='email', validators=[DataRequired(), Email()])
    userName = StringField('userName', id='userName', validators=[DataRequired(), Length(min=1, max=255)])
    phone = StringField('phone', id='phone', validators=[DataRequired()])
    address = HiddenField('address', id='address', validators=[DataRequired()])