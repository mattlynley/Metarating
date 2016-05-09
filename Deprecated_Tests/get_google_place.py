import urllib2
import json

keyword = '%22la%20paella%22'

latlong = '40.729649,-73.988446'
auth_key = 'AUTHKEYGOESHERE'
radius = '5000'

url = ('https://maps.googleapis.com/maps/api/place/search/json?'
      'name=%s&'
      'location=%s&'
      'sensor=false&'
      'radius=%s&'
      'key=%s') % (keyword, latlong, radius, auth_key)

response = urllib2.urlopen(url)

json_raw = response.read()
json_data = json.loads(json_raw)

print json_data

print "The rating for %s is %s" % (json_data['results'][0]['name'], 
								   json_data['results'][0]['rating'])
print 'The photo reference is:' + json_data['results'][0]['photos'][0]['photo_reference']

google_photo_id = json_data['results'][0]['photos'][0]['photo_reference']

url2 = url = ('https://maps.googleapis.com/maps/api/place/photo?'
			   'maxwidth=640&'
			   'photoreference=%s&'
			   'sensor=true&'
			   'key=%s') % (google_photo_id, auth_key)

print 'The URL is' + url2
