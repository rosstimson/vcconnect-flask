from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, SubmitField, IntegerField
from wtforms.validators import Required, Optional
from .vcconnect import get_main_area_dropdown


class MainAreaForm(FlaskForm):
    choices = get_main_area_dropdown()
    main_area = SelectField('Main Area',
                            coerce=int,
                            choices=get_main_area_dropdown(),
                            validators=[Required()])
    submit = SubmitField('Submit')


class VenueSearchForm(FlaskForm):
    area_id = SelectField('Area',
                          coerce=int,
                          choices=get_main_area_dropdown(),
                          validators=[Required()])
    venue_car_parking = BooleanField('Car Parking')
    disabled = BooleanField('Disabled Parking')
    catering = BooleanField('Catering')
    event_management = BooleanField('Event Management')
    hearing = BooleanField('Hearing Loop')
    photocopy = BooleanField('Photocopying')
    refreshments = BooleanField('Refreshments')
    wheelchair = BooleanField('Wheelchair Access')
    max_capacity = IntegerField('Room Capacity', validators=[Optional()])
    submit = SubmitField('Submit')
