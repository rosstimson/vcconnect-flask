import requests
import os


# TODO:  How can we use app.config here rather than env var from OS.
API_KEY = os.environ.get('VCC_API_KEY')
BASE_URL = 'https://www.vcconnectsystem.org.uk/api/'


def remove_underscores(string):
    return string.replace('_', '')


def get_main_area_dropdown():
    r = requests.post(BASE_URL + 'GetMainAreaList',
                      json={"apikey": API_KEY})
    main_area_list = r.json()
    main_area_dropdown_items = []

    for i in main_area_list:
        main_area_dropdown_items.append((i['MainAreaID'], i['MainArea']))
    return main_area_dropdown_items


def get_venues(**kwargs):
    json = {"apikey": API_KEY}
    for k, v in kwargs.items():
        json[remove_underscores(k)] = v
    print(json)
    r = requests.post(BASE_URL + 'GetVenueList',
                      json=json)
    venue_list = r.json()
    return venue_list


def get_orgs_by_main_area(main_area_id):
    r = requests.post(BASE_URL + 'GetOrganisationList',
                      json={"apikey": API_KEY,
                            "MainAreaID": main_area_id})
    org_list = r.json()
    return org_list


def get_org_details(org_id):
    r = requests.post(BASE_URL + 'GetOrganisationDetails',
                      json={"apikey": API_KEY,
                            "OrgID": org_id})
    org_details = r.json()
    return org_details
