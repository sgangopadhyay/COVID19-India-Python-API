# NAME # SUMAN GANGOPADHYAY
# PROGRAM # Python program to fetch COVID19 data from Government of India API Server
# URL # https://api.covid19india.org/data.json
# LANGUAGE # Python 3.9

import requests

def covid19_state_total_case(state, url):
    state = state.lower()
    json_data = requests.get(url).json()    
    for i in range(0, 30):
        if state == json_data['statewise'][i]['state'].lower():
            confirmed = json_data['statewise'][i]['confirmed']
            active = json_data['statewise'][i]['active']
            deaths = json_data['statewise'][i]['deaths']
    return {'state':state,'confirmed_cases':confirmed, 'active_cases':active, 'deaths':deaths}
    
url = "https://api.covid19india.org/data.json"
print(covid19_state_total_case('delhi',url))
