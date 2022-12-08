from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired(),Length(min=3, max=20)],)
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



    # user_name = SearchField('user_name',validators=[DataRequired(),Length(min=2,max=20)])
    # last_name = SearchField('last_name',validators=[DataRequired(),Length(min=2,max=20)])
    # phon_number = SearchField('phon_number',validators=[DataRequired(),Length(min=2,max=20)])
    # location = SearchField('location',validators=[DataRequired(),Length(min=2,max=20)])
    # gender = SearchField('gender',validators=[DataRequired(),Length(min=2,max=20)])
    # interested_in = SearchField('interested_in',validators=[DataRequired(),Length(min=2,max=20)])
    # hobbies = SearchField('hobbies',validators=[DataRequired(),Length(min=2,max=20)])
    # friends = SearchField('friends',validators=[DataRequired(),Length(min=2,max=20)])
