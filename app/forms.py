from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    rooms = StringField('No. of Rooms', validators=[InputRequired()])
    baths = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Property Type', choices = [('house', 'House'), ('apt', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])