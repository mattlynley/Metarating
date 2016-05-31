import foursquare
import newAPIs
# class APIs(object):
	
# 	def __init__(self):

# 		self.foursquare_client_id = 'GINF1JS3KJQXGXZUKMDAQS42DWH1AY0R2XCMHBD23GKK5JZE'
# 		self.foursquare_client_secret = 'PLICU3RXKGJSOQOJZSRFHQRZYADZMEXWMKTJ1LMFQFR0MBQC'

# 		self.google_auth_key = 'AIzaSyCoOa7FM_7OmFWCUcrg3lhORHNZPKiHRuQ'

# 		self.yelp_consumer_key = 'iBTdR4SaePT8gpSTTxs_vA'
# 		self.yelp_consumer_secret = 'Dw5iz0ZEMOK50Fkcyfl8Hk65Rik'
# 		self.yelp_token = 'aQiyZMRn9RxwXSVQTNusyEHzihMZIk2x'
# 		self.yelp_token_secret = 'IPSv1Ygu84z7eFiHnTbLIRXQrVQ'

# 		self.twilio_account_sid = "AC2ba222b8072e4fb7c4abe4e7e31b7811"
# 		self.twilio_auth_token = "cc976a4439c9ef3c81c5ae49625c89a4"

# 		self.twilionumberto = "+18324834899"
# 		self.twilionumberfrom = "+19362294161"

# class foursquare(object)

# 	def __init__(self):

# 		client = foursquare.Foursquare(client_id = foursquare_client_id,
# 									client_secret= foursquare_client_secret)

# 		neighborhood = raw_input("Please enter a neighborhood: ")
# 		city = raw_input("Please enter a city")

# 		venue_raw = client.venues.search(params={'squery': neighborhood,
# 										'near': city})

# 		print venue_raw


script_apis = newAPIs.APIs()

foursquare_client_id = script_apis.foursquare_client_id
foursquare_client_secret = script_apis.foursquare_client_secret

client = foursquare.Foursquare(client_id = foursquare_client_id, 
						client_secret= foursquare_client_secret)

neighborhood = raw_input('Please enter the local neighborhood\n> ')
city = raw_input('Please enter the city and state\n>')

venue_raw = client.venues.search(params={'query': neighborhood, 'near': city})

latitude = venue_raw['venues'][0]['location']['lat']

print latitude

longitude = venue_raw['venues'][0]['location']['lng']

print longitude

latlong = str(latitude) + ', ' + str(longitude)

venue = raw_input("Please enter what you're looking for\n")

i = 0

newratingarray = []

while i < 50:

	venue_raw = client.venues.search(params={'query': venue, 'll': latlong})

	print("Here's the new name for the bar:")

	print(venue_raw['venues'][i]['name'])

	venue_raw_two = client.venues.search(params={'query': venue_raw['venues'][i]['name'], 'll': latlong})

	print("Now let's get the ID and plug it in\n")

	venue_raw_two_id = venue_raw_two['venues'][0]['id']

	newvenue_raw_two = client.venues(venue_raw_two_id)

	print("Is there a rating in it?\n")

	if 'rating' in newvenue_raw_two['venue']:
		print("There's a rating here and it is: " + str(newvenue_raw_two['venue']['rating']))
		newratingarray.append([venue_raw['venues'][i]['name'], str(newvenue_raw_two['venue']['rating'])])
	else:
		print("Nope, there's no rating")

	i += 1

print("Here are the venues that have ratings and their scores:\n")

print(newratingarray)