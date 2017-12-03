from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, SubmitField, IntegerField
from wtforms.validators import Required, Optional
from .vcconnect import get_main_area_dropdown, get_service_dropdown, get_client_group_dropdown


class OrgSearchForm(FlaskForm):
    main_area_id = SelectField('Area',
                               coerce=int,
                               choices=get_main_area_dropdown(),
                               validators=[Optional()])
    service_id = SelectField('Service',
                               coerce=int,
                               choices=get_service_dropdown(),
                               validators=[Optional()])
    client_group_id = SelectField('Client Group',
                               coerce=int,
                               choices=get_client_group_dropdown(),
                               validators=[Optional()])
    submit = SubmitField('Submit')


class VenueSearchForm(FlaskForm):
    area_id = SelectField('Area',
                          coerce=int,
                          choices=get_main_area_dropdown(),
                          validators=[Optional()])
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
