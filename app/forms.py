from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField,StringField,SelectField,TextAreaField,SubmitField
from wtforms import validators

class CreationForm(FlaskForm):
    first_name = TextField('First Name', [validators.Required("Please enter a first name")])
    last_name = TextField('Last Name', [validators.Required("Please enter a last name")])
    location = TextField('Location', [validators.Required("Please enter a location")])
    gender = SelectField('Gender', choices=[('N/A', 'Select Gender'),('M', 'Male'), ('F', 'Female')])
    email = TextField("Email",[validators.Required("Your need to enter an email"),validators.Email("Enter a valid email")])
    bio = TextAreaField('Biography')
    photo = FileField("Profile Picture",validators = [FileRequired(),FileAllowed(['jpg','png','jpeg'])])    
    submit = SubmitField("Add Profile")