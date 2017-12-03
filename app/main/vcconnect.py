import requests
import os


# TODO:  How can we use app.config here rather than env var from OS.
API_KEY = os.environ.get('VCC_API_KEY')
BASE_URL = 'https://www.vcconnectsystem.org.uk/api/'


def remove_underscores(string):
    return string.replace('_', '')


def remove_null_options(dic):
    dic = dic
    delete = []

    for k, v in dic.items():
        if v == 0:
            delete.append(k)

    for i in delete:
        del dic[i]

    return dic


def displayable(lst, address_id):
    for i, dic in enumerate(lst):
        if dic['AddressID'] == int(address_id):
            if dic['Expired'] == False and dic['InformationMadePublic'] == True:
                return True
    return False


def get_main_area_dropdown():
    r = requests.post(BASE_URL + 'GetMainAreaList',
                      json={"apikey": API_KEY})
    main_area_list = r.json()
    main_area_dropdown_items = [(0, '--- Any ---')]

    for i in main_area_list:
        main_area_dropdown_items.append((i['MainAreaID'], i['MainArea']))
    return main_area_dropdown_items


def get_client_group_dropdown():
    r = requests.post(BASE_URL + 'GetClientGroupList',
                      json={"apikey": API_KEY})
    client_group_list = r.json()
    client_group_dropdown_items = [(0, '--- Any ---')]

    for i in client_group_list:
        client_group_dropdown_items.append((i['ClientGroupID'], i['ClientGroup']))
    return client_group_dropdown_items


def get_service_dropdown():
    r = requests.post(BASE_URL + 'GetServiceList',
                      json={"apikey": API_KEY})
    service_list = r.json()
    service_dropdown_items = [(0, '--- Any ---')]

    for i in service_list:
        service_dropdown_items.append((i['ServiceID'], i['Service']))
    return service_dropdown_items


def get_venues(**kwargs):
    json = {"apikey": API_KEY}
    for k, v in kwargs.items():
        json[remove_underscores(k)] = v

    remove_null_options(json)

    # TODO: Proper logging for DEBUG here.
    print(json)

    r = requests.post(BASE_URL + 'GetVenueList',
                      json=json)
    venue_list = r.json()
    return venue_list


def get_orgs(**kwargs):
    json = {"apikey": API_KEY}
    for k, v in kwargs.items():
        json[remove_underscores(k)] = v

    remove_null_options(json)

    # TODO: Proper logging for DEBUG here.
    print(json)

    r = requests.post(BASE_URL + 'GetOrganisationList',
                      json=json)
    org_list = r.json()
    return org_list


def get_org_details(org_id):
    all_orgs = get_orgs()
    r = requests.post(BASE_URL + 'GetOrganisationDetails',
                      json={"apikey": API_KEY,
                            "OrgID": org_id})
    org_details = r.json()
    return org_details
