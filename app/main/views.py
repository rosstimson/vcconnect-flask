from flask import render_template, session, redirect, url_for, request, session
from . import main
from .forms import MainAreaForm
from .vcconnect import get_orgs_by_main_area, get_org_details


@main.route('/', methods=['GET', 'POST'])
def index():
    form = MainAreaForm()
    if form.validate_on_submit():
        session['main_area'] = form.main_area.data
        return redirect(url_for('.org_results'))
    return render_template('index.html', form=form, main_area=session.get('main_area'))


@main.route('/org_results')
def org_results():
    results = get_orgs_by_main_area(session.get('main_area'))
    return render_template('org_results.html', results=results)


@main.route('/org')
def org():
    org_id = request.args.get('id')
    org_details = get_org_details(org_id)
    return render_template('org_details.html', org_details=org_details)
