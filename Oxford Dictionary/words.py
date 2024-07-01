import json
import requests
from random import choice

app_id = "<your app id>"
app_key = "<your gmail app password>"
language = "en-us"
word_id = "ace"
url = "https://od-api-sandbox.oxforddictionaries.com:443/api/v2/thesaurus/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
word_data = r.json()

print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
with open("words.txt", "w") as f:
    json.dump(word_data, f, indent=2)

