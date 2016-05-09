import foursquare

foursquare_client_id = 'APIKEYGOESHERE'

foursquare_client_secret = 'APIKEYGOESHERE'

client = foursquare.Foursquare(client_id = foursquare_client_id, 
						client_secret= foursquare_client_secret)

neighborhood = raw_input('Please enter the local neighborhood\n> ')
city = raw_input('Please enter the city and state\n>')

venue_raw = client.venues.search(params={'query': neighborhood, 'near': city})

print venue_raw

latitude = venue_raw['venues'][0]['location']['lat']

print latitude

longitude = venue_raw['venues'][0]['location']['lng']

print longitude

latlong = str(latitude) + ', ' + str(longitude)

print 'The latitude and longitude of the neighborhood is: ' + latlong

## now let's try getting the venue

venue = raw_input('Please enter the name of the venue\n> ')

venue_raw_two = client.venues.search(params={'query': venue, 'll': latlong})

print venue_raw_two

venue_id = venue_raw_two['venues'][0]['id']
venue_id_two = venue_raw_two['venues'][1]['id']



def gogo():
	i=0
	while True:
		try:
			return client.venues(venue_raw_two['venues'][i]['id'])['venue']['rating']
		except KeyError:
			pass
		i += 1

print gogo()
