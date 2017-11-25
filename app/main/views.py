from flask import render_template, session, redirect, url_for, request, session
from . import main
from .forms import MainAreaForm
from .vcconnect import get_orgs_by_main_area, get_venues_by_main_area, get_org_details


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/orgs', methods=['GET', 'POST'])
def orgs():
    form = MainAreaForm()
    if form.validate_on_submit():
        session['main_area'] = form.main_area.data
        return redirect(url_for('.org_results'))
    return render_template('org_search.html', form=form, main_area=session.get('main_area'))


@main.route('/venues', methods=['GET', 'POST'])
def venues():
    form = MainAreaForm()
    if form.validate_on_submit():
        session['main_area'] = form.main_area.data
        return redirect(url_for('.venue_results'))
    return render_template('venue_search.html', form=form, main_area=session.get('main_area'))


# TODO Repetition here with the results routes otherwise there would
# need to be 2 API calls instead of one, one of which would be
# unnecessary depending on the search being done.
@main.route('/org_results')
def org_results():
    results = get_orgs_by_main_area(session.get('main_area'))
    return render_template('org_results.html', results=results)


@main.route('/venue_results')
def venue_results():
    results = get_venues_by_main_area(session.get('main_area'))
    return render_template('venue_results.html', results=results)


@main.route('/org')
def org():
    org_id = request.args.get('id')
    org_details = get_org_details(org_id)
    return render_template('org_details.html', org_details=org_details)
