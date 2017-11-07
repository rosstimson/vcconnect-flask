from os import environ, environb
from flask import Flask, render_template, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Required

import requests

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = environb.get(b'SECRET_KEY')
app.config['VCC_API_KEY'] = environ.get('VCC_API_KEY')


manager = Manager(app)
bootstrap = Bootstrap(app)

api_key = app.config['VCC_API_KEY']


def get_main_area_dropdown():
    r = requests.post('https://www.vcconnectsystem.org.uk/api/GetMainAreaList', json={"apiKey": api_key})
    main_area_list = r.json()
    main_area_dropdown_items = []

    for i in main_area_list:
        main_area_dropdown_items.append((i['MainAreaID'], i['MainArea']))

    return main_area_dropdown_items


def get_orgs_by_main_area(main_area_id):
    r = requests.post('https://www.vcconnectsystem.org.uk/api/GetOrganisationList', json={"apiKey": api_key, "MainAreaID": main_area_id})
    org_list = r.json()

    return org_list


class MainAreaForm(FlaskForm):
    choices = get_main_area_dropdown()
    area = SelectField('Main Area', coerce=int, choices=choices, validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    area = None
    results = None
    form = MainAreaForm()
    if form.validate_on_submit():
        area = form.area.data
        form.area.data = ''
        results = get_orgs_by_main_area(area)
        return render_template('results.html', results=results)
    return render_template('index.html', form=form, area=area)


@app.route('/results')
def results():
    orgs = get_orgs_by_main_area()


if __name__ == '__main__':
    manager.run()
