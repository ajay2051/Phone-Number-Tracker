import phonenumbers
from test import number
key = "1517237d8c324e26a64de8716f999c90"

from phonenumbers import geocoder

code = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(code, "en")
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
provider = carrier.name_for_number(service_provider, "en")
print(provider)

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)