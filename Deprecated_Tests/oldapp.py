import web
import getrealrating
import apis

urls = (
  '/', 'Index',
  '/result', 'Result'
)
app = web.application(urls, globals())

# this just gets the API keys from a separate script, because we're lazy

script_apis = apis.APIs()

render = web.template.render('templates/')

class Index(object):
    
    def GET(self):

        return render.hello_form()

    def POST(self):

        # This is about to look EXTREMELY ugly so pardon the lack of PEP8
      
    	form = web.input(venue=None, neighborhood=None, 
    					 city=None)
    	
    	venue_object = getrealrating.Ratings(form.venue, form.neighborhood,
    					form.city, script_apis.foursquare_client_id, 
                        script_apis.foursquare_client_secret)

    	venue_object.foursquare_rating = venue_object.get_foursquare_rating()

    	venue_object.google_rating = venue_object.get_google_rating(script_apis.google_auth_key)

        venue_object.google_photo = venue_object.get_google_photo(script_apis.google_auth_key)
        venue_object.yelp_stars = venue_object.get_yelp_star_pic(script_apis.yelp_consumer_key, 
                                   script_apis.yelp_consumer_secret, script_apis.yelp_token,
                                   script_apis.yelp_token_secret)


    	venue_object.yelp_rating = venue_object.get_yelp_rating(script_apis.yelp_consumer_key, 
    							   script_apis.yelp_consumer_secret, script_apis.yelp_token,
    					 		   script_apis.yelp_token_secret)

        venue_object.facebook_likes = venue_object.get_facebook_likes()
        venue_object.facebook_talking_about = venue_object.get_facebook_talking_about()

        venue_object.citygrid_rating = venue_object.get_citygrid_rating()

        venue_object.data = venue_object.get_venue_data()

    	return render.results_page(venue_object)

if __name__ == "__main__":
    app.run()