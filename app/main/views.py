from flask import render_template, session, redirect, url_for, request, session
from . import main
from .forms import OrgSearchForm, VenueSearchForm
from .vcconnect import get_orgs, get_venues, get_org_details, displayable


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/orgs', methods=['GET', 'POST'])
def orgs():
    form = OrgSearchForm()
    if form.validate_on_submit():
        session['main_area_id'] = form.main_area_id.data
        session['service_id'] = form.service_id.data
        session['client_group_id'] = form.client_group_id.data

        return redirect(url_for('.org_results'))
    return render_template('org_search.html', form=form)


# TODO Repetition here with the results routes otherwise there would
# need to be 2 API calls instead of one, one of which would be
# unnecessary depending on the search being done.
@main.route('/org_results')
def org_results():
    main_area_id = session.get('main_area_id')
    service_id = session.get('service_id')
    client_group_id = session.get('client_group_id')

    results = get_orgs(main_area_id=main_area_id,
                       service_id=service_id,
                       client_group_id=client_group_id)
    return render_template('org_results.html', results=results)


@main.route('/org')
def org():
    org_id = request.args.get('id')
    all_orgs = get_orgs()
    if displayable(all_orgs, org_id) == True:
        org_details = get_org_details(org_id)
        return render_template('org_details.html', org_details=org_details)
    else:
        return render_template('404.html'), 404


@main.route('/venues', methods=['GET', 'POST'])
def venues():
    form = VenueSearchForm()
    if form.validate_on_submit():
        session['area_id'] = form.area_id.data
        session['venue_car_parking'] = form.venue_car_parking.data
        session['disabled'] = form.disabled.data
        session['catering'] = form.catering.data
        session['event_management'] = form.event_management.data
        session['hearing'] = form.hearing.data
        session['photocopy'] = form.photocopy.data
        session['refreshments'] = form.refreshments.data
        session['wheelchair'] = form.wheelchair.data
        session['max_capacity'] = form.max_capacity.data

        return redirect(url_for('.venue_results'))
    return render_template('venue_search.html', form=form)


@main.route('/venue_results')
def venue_results():
    area_id = session.get('area_id')
    venue_car_parking = session.get('venue_car_parking')
    disabled = session.get('disabled')
    catering = session.get('catering')
    event_management = session.get('event_management')
    hearing = session.get('hearing')
    photocopy = session.get('photocopy')
    refreshments = session.get('refreshments')
    wheelchair = session.get('wheelchair')
    max_capacity = session.get('max_capacity')

    results = get_venues(area_id=area_id,
                         venue_car_parking=venue_car_parking,
                         disabled=disabled,
                         catering=catering,
                         event_management=event_management,
                         hearing=hearing,
                         photocopy=photocopy,
                         refreshments=refreshments,
                         wheelchair=wheelchair,
                         max_capacity=max_capacity)
    return render_template('venue_results.html', results=results)
