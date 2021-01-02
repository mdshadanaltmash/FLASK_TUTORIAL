from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class AddForm(FlaskForm):
    name=StringField("Owner Name")
    puppy_id=IntegerField("Puppy Id")
    submit=SubmitField("Add Owner")
