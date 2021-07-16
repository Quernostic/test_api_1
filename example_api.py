import requests

response = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json")
print(response)

json_response = response.json()
print(json_response['product'])


