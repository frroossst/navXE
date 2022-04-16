from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class navigationForm(FlaskForm):

    home = StringField("home",validators=[DataRequired(), Length(min=1)])

    destination = StringField("destination",validators=[DataRequired(), Length(min=1)])

    submit = SubmitField("Navigate")