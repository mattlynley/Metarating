## pulled from Yelp API example library
## https://github.com/Yelp/yelp-api/tree/master/v2/python

import oauth2
import urllib2
import json

## so no one steals the keys... this is just on GH

consumer_key = 'GOESHERE'
consumer_secret = 'GOESHERE'
token = 'GOESHERE'
token_secret = 'GOESHERE'

consumer = oauth2.Consumer(consumer_key, consumer_secret)

tags = ''

next = 'foo'

while next:
	next = raw_input('Type in a tag to append\n> ')
	tags += ('&' + next)

print tags

url = 'http://api.yelp.com/v2/search?' + tags

print 'URL: %s' % (url,)

oauth_request = oauth2.Request('GET', url, {})
oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
					  'oauth_timestamp': oauth2.generate_timestamp(),
					  'oauth_token': token,
					  'oauth_consumer_key': consumer_key})

token = oauth2.Token(token, token_secret)

oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

signed_url = oauth_request.to_url()

print 'Signed URL: %s' % (signed_url,)

reader = ''

req = urllib2.Request(signed_url)
response = urllib2.urlopen(req)
raw_yelp_data = json.load(response)

print "The rating for venue %r is %r" % (raw_yelp_data['businesses'][0]['name'], 
								         raw_yelp_data['businesses'][0]['rating'])

print "The number of reviews is %r" % (raw_yelp_data['businesses'][0]['review_count'])
