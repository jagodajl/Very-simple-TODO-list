from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, TextAreaField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Descryption", validators=[DataRequired()])

    done = BooleanField("Task Completed ")