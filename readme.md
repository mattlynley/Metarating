This is mostly just an attempt to learn how to interface with various APIs, for personal use for the time being. Use it when looking for new restaurants in New York without having to cross-reference their scores all the time across multiple apps.

Here's the to-do list:

√ Build an app that collects ratings from Foursquare, Zagat, Yelp and 
  various others for a specific venue in a specific neighborhood.

√ Store all ratings in an object that carries respective API keys and 
  tokens and render a static page with that object.

o Deploy on an Amazon micro-instance using Flask.

√ Impelement geolocation capture and use that to get venue results

o Create a 'weighted' rating system that will correct for Yelp's sloppiness 
  in New York.

o Add a way to search and select from a list of venues given criteria 

o Re-implement Facebook Open Graph data using its Javascript SDK

o Make the web results look better

o Weight the search results with the 'true' weighted rating