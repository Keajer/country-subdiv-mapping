import pycountry
import simplejson as json

country_iso2_2_fullname = dict()
country_fullname_2_iso2 = dict()
for l in pycountry.countries:
    country_iso2_2_fullname[l.alpha2] = l.name
    country_fullname_2_iso2[l.name] = l.alpha2

subdiv_iso_2_fullname = dict()
subdiv_fullname_2_iso = dict()
for l in pycountry.subdivisions:
    subdiv_fullname_2_iso[l.name] = l.code.split('-')[1]
    subdiv_iso_2_fullname[l.code.split('-')[1]] = l.name

country_subdiv_fullname = dict()
country_subdiv_iso = dict()
for l in pycountry.subdivisions:
    if l.country.name not in country_subdiv_fullname:
        country_subdiv_fullname[l.country.name] = [l.name]
    else:
        country_subdiv_fullname[l.country.name].append(l.name)

    if l.country.alpha2 not in country_subdiv_iso:
        country_subdiv_iso[l.country.alpha2] = [l.code]
    else:
        country_subdiv_iso[l.country.alpha2].append(l.code)

def save_2_json(file_name, data):
    with open(file_name, 'wb') as output:
        json.dump(data, output, indent=2)

def main(save_path):
    save_2_json(save_path+'country_iso2_2_fullname.json', country_iso_2_full_name)
    save_2_json(save_path+'country_fullname_2_iso2.json', country_fullname_2_iso2)
    save_2_json(save_path+'subdiv_fullname_2_iso.json', subdiv_fullname_2_iso)
    save_2_json(save_path+'subdiv_iso_2_fullname.json', subdiv_iso_2_fullname)
    save_2_json(save_path+'country_subdiv_iso.json', country_subdiv_iso)
    save_2_json(save_path+'country_subdiv_fullname.json', country_subdiv_fullname)

if __name__ == '__main__':
    save_path = '/User/kanyu/Documents/Branch.io/adhoc/'
    main(save_path)

