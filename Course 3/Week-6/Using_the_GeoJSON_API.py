import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "Ramapo College of New Jersey"

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

'''
Just simple, the structure of GeoJSON:
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "505",
                    "short_name": "505",
                    "types": [
                        "street_number"
                    ]
                },
                ...
            ],
            "formatted_address": "Anywhere",
            "geometry": {
                "location": {
                    "lat": 41.081015,
                    "lng": -74.1745057
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lng": -74.1731567197085
                    },
                    "southwest": {
                        "lat": 41.0796660197085,
                        "lng": -74.17585468029151
                    }
            },
            "place_id": "ChIJZ-40AqThwokR5zVOLCxa-Ro",
            "plus_code": {
                "compound_code": "3RJG+C5 Mahwah, NJ, USA",
                "global_code": "87H73RJG+C5"
            },
                "establishment",
                "point_of_interest",
                "university"
            ]
        }
    ],
}

So just need to access results then go to placeid
'''

location = js['results'][0]['place_id']
print(location)