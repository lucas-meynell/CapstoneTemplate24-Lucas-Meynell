# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, NumberRange
from wtforms.fields.html5 import URLField, DateField, IntegerRangeField, EmailField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, RadioField
from wtforms_components import TimeField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    role = SelectField('Role', choices=[("Teacher", "Teacher"),("Student", "Student")])
    age = StringField('Age', validators=[DataRequired()])
    image = FileField("Image") 
    submit = SubmitField('Post')

class ConsentForm(FlaskForm):
    adult_fname = StringField('First Name',validators=[DataRequired()])
    adult_lname = StringField('Last Name',validators=[DataRequired()])
    adult_email = EmailField('Email',validators=[Email()])
    consent = RadioField('Do you want your parents or teachers to see your sleep data/graph', choices=[(True,"True"),(False,"False")])
    submit = SubmitField('Submit')

class SleepForm(FlaskForm):
    rating = SelectField("How good was the food: 5 is great, 1 is poor", choices=[(None,'---'),(1,1),(2,2),(3,3),(4,4),(5,5)])
    foodname = StringField("What did you eat")   
    meal = SelectField("What meal was this for?", choices=[(None,'---'),("Breakfast","breakfast"),("Lunch","lunch"),("Dinner","dinner")])   
    feel = SelectField("How did you feel after eating this food: 5 is healthy, 1 is guilty", choices=[(None,'---'),(1,1),(2,2),(3,3),(4,4),(5,5)])
    mealdate = DateField("What date did you eat this food")
    totalmeals = IntegerField("How many total meals have you had today?", validators=[NumberRange(min=0,max=180, message="Enter a number between 0 and 180.")])
    submit = SubmitField("Submit")

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Food(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    createdate = DateField("When did you have this")
    foodname = StringField()
    foodrating = StringField('Rating', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])