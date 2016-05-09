import urllib2
import json

url = ('http://api.citygridmedia.com/content/places/v2/search/latlon?'
	   'what=la%20paella'
	   '&lat=40.729649'
	   '&lon=-73.988446'
	   '&radius=5'
	   '&publisher=test&'
	   'format=json')

response = urllib2.urlopen(url)

json_raw = response.read()
json_data = json.loads(json_raw)

rating = json_data['results']['locations'][0]['rating']

print rating