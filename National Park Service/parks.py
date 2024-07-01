
import json
import requests

def get_park_data(api_key):
    base_url = "https://developer.nps.gov/api/v1/activities/parks/"
    HEADERS = {"x-api-key":api_key}
    response = requests.get(base_url, headers=HEADERS)
    data = response.json()
    return data

api_key = "<your api key here>"

park_data = get_park_data(api_key)

with open("national_parks.json", "w") as f:
    json.dump(park_data, f, indent=2)

with open("national_parks.json") as f:
    parks = json.load(f)

park_set = (parks['data'])
all_parks = set()
for park_info in park_set[:]:
    park = park_info['parks']
    
    for index, cur_park in enumerate(park):
        if cur_park['designation'] == 'National Park':
            all_parks.add((cur_park['fullName'], cur_park['states'], cur_park['url']))

print(f"There are {len(all_parks)} national parks in the US.")
sorted_parks = sorted(all_parks)
for park_name in sorted_parks:
    print(park_name)

with open("all_national.json", "w", encoding="utf-8") as f:
    json.dump(sorted_parks, f, indent=2, ensure_ascii=False, sort_keys=True)
