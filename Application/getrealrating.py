import foursquare
import oauth2
import urllib2
import json
import requests

class Ratings(object):

	def __init__(self, venue, neighborhood, city, 
				 foursquare_client_id, foursquare_client_secret,
				 inputlatitude, inputlongitude):

		"""Initializes an object with venue/location.

		We'll get the lat-long in the constructor using Foursquare,

		unless it's captured by the browser."""

		self.neighborhood = neighborhood
		self.city = city
		self.venue = venue
		self.foursquare_client_id = foursquare_client_id
		self.foursquare_client_secret = foursquare_client_secret
		self.inputlatitude = inputlatitude
		self.inputlongitude = inputlongitude

		# We're going to use the client again later, so initialize here as
		# self for future use.

		self.client = foursquare.Foursquare(client_id = self.foursquare_client_id, 
									client_secret= self.foursquare_client_secret)

		if self.city and self.city.lower() != "enter a city":
			venue_raw = self.client.venues.search(params={'query': self.neighborhood, 
													 'near': self.city})

			self.latitude = venue_raw['venues'][0]['location']['lat']
			self.longitude = venue_raw['venues'][0]['location']['lng']
			self.location = str(self.latitude) + ',' + str(self.longitude)
		else:
			self.latitude = inputlatitude
			self.longitude = inputlongitude
			self.location = str(self.latitude) + ',' + str(self.longitude)
		
		# We'll use the raw data with lat-long a couple times later so we'll
		# intialize it in the constructor.

		self.foursquare_venue_raw = (
				self.client.venues.search(params={'query': self.venue, 
											      'll': self.location}))

	def get_foursquare_data(self):

		"""Fetches the data for a venue from Foursquare.

		This includes venue data like name, location as well

		as the rating of the venue."""

		foursquare_return = {}

		i = 0
		j = 0

		## First, a hack to get the score, because the first venue
		## might not always be the one we're looking for. A venue with
		## the word "park" in the name is a good example of this.

		while True:
			try:
				venue_id = self.foursquare_venue_raw['venues'][i]['id']
				venue_specific_raw = self.client.venues(venue_id)
				foursquare_return['score'] = venue_specific_raw['venue']['rating']
				break
			except KeyError:
				pass
			i += 1

		## We'll also use Foursquare to get the proper naming and
		## formatting for the venue. Stuck in one function to save API
		## calls.

		foursquare_return_data = {}

		foursquare_return_data['venue_name'] = (
			self.foursquare_venue_raw['venues'][i]['name'])

		foursquare_return['data'] = foursquare_return_data

		foursquare_venues = []

		while True:
			try:
				foursquare_venues.append(
					self.foursquare_venue_raw['venues'][j]['name'])
			except IndexError:
				break
			j+=1

			if j == 10:
				break

		foursquare_return['venue_list'] = foursquare_venues

		## More stuff to come here, later, once we clean up the HTML output.
		## We'll capture tips at some point, too.

		return foursquare_return

	def get_google_data(self, auth_key):

		"""Fetches a venue's data from Google using the places

		API. We'll get the photo and score in this method."""

		# First, a hack to deal with spaces in the venue name. Google
		# requires you to wrap a venue with %22 to deal with spaces.

		venue_words = self.venue.split(' ')
		google_venue = '%22'

		for i in range(len(venue_words)):
			if i == range(len(venue_words)):
				google_venue+= venue_words[i]
			else:
				google_venue+= venue_words[i] + '%20'

		google_venue+= '%22'

		url = ('https://maps.googleapis.com/maps/api/place/search/json?'
		      'name=%s&'
		      'location=%s&'
		      'sensor=false&'
		      'radius=10000&'
		      'key=%s') % (google_venue, self.location, auth_key)

		json_raw = urllib2.urlopen(url).read()
		json_data = json.loads(json_raw)

		google_return = {}

		## We'll just get all the data in this function so we only have
		## to do one API call to Google. First, get the rating.

		try:
			google_rating_final = json_data['results'][0]['rating']
			google_return['score'] = google_rating_final
		except:
			google_return['score'] = None

		## Then get the URL of the photo.

		try:
			google_photo_id = json_data['results'][0]['photos'][0]['photo_reference']
			url = ('https://maps.googleapis.com/maps/api/place/photo?'
			   'maxwidth=640&'
			   'photoreference=%s&'
			   'sensor=true&'
			   'key=%s') % (google_photo_id, auth_key)
			google_return['photo_url'] = url
		except:
			google_return['photo_url'] = None

		## And then ship both off to the server

		return google_return

	def get_yelp_data(self, consumer_key, consumer_secret,
							  token, token_secret):

		"""Fetches all the Yelp data using Yelp's API.

		This uses oAuth so we'll just leave it as a single

		API call."""

		consumer = oauth2.Consumer(consumer_key, consumer_secret)

		tags = 'term=' + self.venue + '&ll=' + self.location
		url = 'http://api.yelp.com/v2/search?' + tags

		oauth_request = oauth2.Request('GET', url, {})
		oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
							  'oauth_timestamp': oauth2.generate_timestamp(),
							  'oauth_token': token,
							  'oauth_consumer_key': consumer_key})

		token = oauth2.Token(token, token_secret)

		oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)

		signed_url = oauth_request.to_url()

		req = urllib2.Request(signed_url)
		response = urllib2.urlopen(req)
		raw_yelp_data = json.load(response)

		## Same thing as Google, we'll get everything we need in one function.
		## Yelp requires oAuth so best to minimize as many calls as we can.

		yelp_rating = raw_yelp_data['businesses'][0]['rating']
		yelp_star_pic = raw_yelp_data['businesses'][0]['rating_img_url']
		yelp_review_count = raw_yelp_data['businesses'][0]['review_count']

		yelp_return_data = {'rating': yelp_rating,
						    'star_url': yelp_star_pic,
						    'review_count': yelp_review_count}

		return yelp_return_data

	def get_citygrid_rating(self):

		"""Fetches Citygrid rating."""

		# First need to handle the whole space-in-venue thing

		venue_words = self.venue.split(' ')
		citygrid_venue = ''

		for i in range(len(venue_words)):
			if i == range(len(venue_words)):
				citygrid_venue+= venue_words[i]
			else:
				citygrid_venue+= venue_words[i] + '%20'

		url = ('http://api.citygridmedia.com/content/places/v2/search/latlon?'
	   'what=%s'
	   '&lat=%s'
	   '&lon=%s'
	   '&radius=5'
	   '&publisher=test'
	   '&format=json') % (citygrid_venue, self.latitude, self.longitude)

		# Might not return a venue, CityGrid isn't comprehensive. So
		# check for that.

		try:
			response = urllib2.urlopen(url)
		except urllib2.URLError:
			return "Couldn't get CityGrid data."

		json_raw = response.read()
		json_data = json.loads(json_raw)

		try:
			return json_data['results']['locations'][0]['rating']
		except:
			return "Couldn't get CityGrid data."
			

	def weight_ratings(self, yelp_rating, yelp_review_count, 
						foursquare_rating, google_rating,
						citygrid_rating):

		"""Weights ratings per inbound review.

		This is somewhat subjective for now, based on experience."""

		## Start with a total surplus to divvy up if certain scores aren't
		## available.

		surplus = 1.0
		coefficients = {}
		scores= {}

		## The worst review possible is a "4 star" on Yelp, which basically tells
		## the consumer nothing. So we'll have to find
		## a way to essentially correct for this. If Yelp ends up being 4 stars, it
		## will scale to the number of reviews (very aggressive prejudice). If it is
		## not, then it will come in as a flat value for now.

		## Even still, we only want Yelp to contribute around 25% of the score.

		try:
			scores['yelp'] = float(yelp_rating)*2

			if float(yelp_review_count) >= 500:

				coefficients['yelp'] = .25
				yelp_surplus = 0

			elif scores['yelp'] == '4.0':

				coefficients['yelp'] = (
					.25 * (float(yelp_review_count)/500))

				yelp_surplus += .25 - coefficients['yelp']

			else:

				coefficients['yelp'] = .25
				yelp_surplus = 0

			surplus -= .25

		except:
			scores['yelp'] = 0

		try:
			scores['google'] = float(google_rating)*2
			coefficients['google'] = .25
			surplus -= .25
		except:
			scores['google'] = 0

		try:
			scores['foursquare'] = float(foursquare_rating)
			coefficients['foursquare'] = .40
			surplus -= .40
		except:
			scores['foursquare'] = 0

		try:
			scores['citygrid'] = float(citygrid_rating)
			coefficients['citygrid'] = .10
			surplus -= .10
		except:
			scores['citygrid'] = 0

		## Now split up the surplus, if certain scores didn't come in.

		for entry in coefficients:
			coefficients[entry] += surplus/len(coefficients)

		for entry in coefficients:
			try:	
				coefficients[entry] += yelp_surplus/len(coefficients)
			except:
				pass

		## Do something with Facebook Likes here

		score_returner = 0

		for entry in coefficients:
			try:
				score_returner += scores[entry]*coefficients[entry]
			except KeyError:
				pass

		weighted_score = round(score_returner, 2)

		if weighted_score > 7:
			color = 'green'
		elif weighted_score <= 7 and weighted_score > 5:
			color = 'yellow'
		else:
			color = 'red'

		weighted_return = {'weighted_score': weighted_score,
						   'weighted_color': color}

		return weighted_return