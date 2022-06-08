from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class MoviesForm(FlaskForm):
    id = IntegerField('id')
    original_title = StringField('title')
    production_year = IntegerField('production year')
    duration = IntegerField('duration(min)')
    type = StringField('movie type')
    description = StringField('description')
    poster_path = StringField('poster path')