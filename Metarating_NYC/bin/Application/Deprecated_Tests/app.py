from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import getrealrating
import newAPIs

script_apis = newAPIs.APIs()

application = Flask(__name__)
application.debug=True

@application.route("/", methods=['GET', 'POST'])
def hello(venue_object=None):
    
    if request.method == 'POST':

        venue_object = getrealrating.Ratings(request.form['venue'], 
                        request.form['neighborhood'], request.form['city'], 
                        script_apis.foursquare_client_id, 
                        script_apis.foursquare_client_secret)

        venue_object.foursquare_rating = venue_object.get_foursquare_rating()

        venue_object.google_rating =     venue_object.get_google_rating(
                                         script_apis.google_auth_key)

        venue_object.google_photo =      venue_object.get_google_photo(
                                         script_apis.google_auth_key)

        venue_object.yelp_stars =        venue_object.get_yelp_star_pic(
                                         script_apis.yelp_consumer_key, 
                                         script_apis.yelp_consumer_secret, 
                                         script_apis.yelp_token,
                                         script_apis.yelp_token_secret)

        venue_object.yelp_rating =       venue_object.get_yelp_rating(
                                         script_apis.yelp_consumer_key, 
                                         script_apis.yelp_consumer_secret, 
                                         script_apis.yelp_token,
                                         script_apis.yelp_token_secret)

        venue_object.facebook_likes = venue_object.get_facebook_likes()
        venue_object.facebook_talking_about = venue_object.get_facebook_talking_about()

        venue_object.citygrid_rating = venue_object.get_citygrid_rating()

        venue_object.data = venue_object.get_venue_data()
    
    return render_template('hello.html', venue_object=venue_object)

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)