from flask import render_template, session, redirect, url_for, request
from . import main
from .forms import MainAreaForm
from .vcconnect import get_orgs_by_main_area, get_org_details


@main.route('/', methods=['GET', 'POST'])
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


@main.route('/results')
def results():
    orgs = vcconnect.get_orgs_by_main_area()



@main.route('/org')
def org():
    org_id = request.args.get('id')
    org_details = get_org_details(org_id)
    return render_template('org_details.html', org_details=org_details)
