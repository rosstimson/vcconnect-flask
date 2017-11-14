import requests
import os

# TODO:  How can we use app.config here rather than env var from OS.
api_key = os.environ.get('VCC_API_KEY')


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
