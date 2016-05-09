from flask import *
import getrealrating
import newAPIs
from twilio.rest import TwilioRestClient

script_apis = newAPIs.APIs()
application = Flask(__name__)

## Use Twilio to catch bugs

twilio_client = TwilioRestClient(script_apis.twilio_account_sid, 
                                  script_apis.twilio_auth_token)

def error_message(error, formdata):

    text_error = (error + "; Venue: " + formdata['venue'] 
                  + "; Neighborhood: "
                  + formdata['neighborhood'] + "; City: "
                  + formdata['city'] + "; Lat: "
                  + formdata['latitude'] + "; Lon: " 
                  + formdata['longitude'])

    message = twilio_client.sms.messages.create(body=str(text_error),
                                         to=script_apis.twilionumberto,
                                         from_=script_apis.twilionumberfrom)

@application.route("/", methods=['GET', 'POST'])
def home(venue_object=None):
    
    return render_template('hello.html')

@application.route("/results", methods=['GET', 'POST'])
def results(venue_object=None):

    venue_object = {}

    venue_object['foursquare_rating'] = request.form['foursquare_rating']
    venue_object['foursquare_name'] = request.form['foursquare_name']
    venue_object['google_rating'] = request.form['google_rating']
    venue_object['google_photo'] = request.form['google_photo']
    venue_object['yelp_stars'] = request.form['yelp_stars']
    venue_object['yelp_review_count'] = request.form['yelp_review_count']
    venue_object['yelp_rating'] = request.form['yelp_rating']
    venue_object['weighted_rating'] = request.form['weighted_score']
    venue_object['background_color'] = request.form['weighted_color']

    return render_template('results.html', venue_object=venue_object)

@application.route("/list", methods=['GET', 'POST'])
def list(venue_object=None, error=None):
    
    # Basically we want the search form to always be there so you
    # can chain through multiple results. We'll figure out a way
    # to cache the results so you can compare multiple and get
    # recommendations.

    # We'll try to catch as many errors as we can and report them
    # via text message (Twilio) to handle them for now.

    formdata = {'venue': request.form['venue'].lower(), 
                'neighborhood': request.form['neighborhood'].lower(), 
                'city': request.form['city'].lower(), 
                'latitude': request.form.get('latitude', 'None'),
                'longitude': request.form.get('longitude', 'None')}

    if (formdata['longitude'] == "None" and formdata['city'] == 'enter a city'):
        
        error = "Need to either specify location or use current location"
        error_message(error, formdata)

        return render_template('venue_object_error.html', 
                                venue_object=None, error=error)

    try:
        venue_object =  getrealrating.Ratings(formdata['venue'], 
                    formdata['neighborhood'], 
                    formdata['city'],
                    script_apis.foursquare_client_id,
                    script_apis.foursquare_client_secret,
                    formdata['latitude'],
                    formdata['longitude'])
    except:
        error = "Couldn't build venue object."
        error_message(error, formdata)

        return render_template('venue_object_error.html', 
                                venue_object=None, error=error)
    
    # Easier to just add attributes to the object and fetch in the HTML
    # Also it looks kind of cleaner. Kind of.

    try:
        foursquare_data = venue_object.get_foursquare_data()
        venue_object.foursquare_rating = foursquare_data['score']
        venue_object.data = foursquare_data['data']
    except:
        error = "Couldn't get Foursquare data."
        error_message(error, formdata)

        return render_template('venue_object_error.html', 
                                venue_object=None, error=error)

    google_data = venue_object.get_google_data(script_apis.google_auth_key)

    try: 
        venue_object.google_rating = google_data['score']
        venue_object.google_photo  = google_data['photo_url']
    except:
        error = "Couldn't get Google data."
        error_message(error, formdata)

        return render_template('venue_object_error.html', 
                                venue_object=None, error=error)

    try:
        yelp_data = venue_object.get_yelp_data(script_apis.yelp_consumer_key, 
                                               script_apis.yelp_consumer_secret, 
                                               script_apis.yelp_token,
                                               script_apis.yelp_token_secret)

        venue_object.yelp_stars = yelp_data['star_url']
        venue_object.yelp_review_count = yelp_data['review_count']
        venue_object.yelp_rating = yelp_data['rating']

    except:
        error = "Couldn't get Yelp data."
        error_message(error, formdata)

        return render_template('venue_object_error.html', 
                                venue_object=None, error=error)

    venue_object.citygrid_rating   = venue_object.get_citygrid_rating()

    try:
         weighted_data = venue_object.weight_ratings(
                         venue_object.yelp_rating,
                         venue_object.yelp_review_count,
                         venue_object.foursquare_rating,
                         venue_object.google_rating,
                         venue_object.citygrid_rating)

         venue_object.weighted_rating = weighted_data['weighted_score']
         venue_object.background_color = weighted_data['weighted_color']

    except:
        error = "Couldn't weight ratings."
        error_message(error, formdata)

        return render_template('venue_object_error.html', 
                                venue_object=None, error=error)
    
    ## This checks to see if there are any obvious words that would identify
    ## the venue. Such as typing "grumpy", there is obviously only one "cafe grumpy"

    ignored_words = ['cafe', 'bar', 'the']
    serialized_venue = formdata['venue'].split(' ')
    for word in ignored_words:
        if word in serialized_venue:
            serialized_venue.remove(word)

    venue_words_split = venue_object.data['venue_name'].split(' ')
    lowercase_venue = []
    for word in venue_words_split:
        lowercase_venue.append(word.lower())

    venue_object.lowercase_venue = lowercase_venue
    venue_object_serialized_venue = serialized_venue

    for word in serialized_venue:
        if word in lowercase_venue:
            venue_object.redirect = True

    ## This checks to see if the venue is obviously not anywhere on the list,
    ## which means you're searching for it under a pseudonym or different name

    lower_venues = []
    for venue in foursquare_data['venue_list']:
        lower_venues.append(venue.lower())

    flag = True

    for i in range(len(lower_venues)):
        if formdata['venue'].lower() in lower_venues[i].split(' '):
            flag = False

    if flag:
        venue_object.redirect = True

    ## Finally, we check if you actually specified the correct venue in
    ## the search. If you did, we return that. If not, and neither of the
    ## cases above are true, we assume you weren't accurate enough and
    ## give you a list of results.

    if formdata['venue'].lower() != venue_object.data['venue_name'].lower():
        venue_object.venue_list = foursquare_data['venue_list']
    else:
        venue_object.redirect = True

    return render_template('list.html', venue_object=venue_object)

if __name__ == '__main__':
    application.debug = True
    application.run()