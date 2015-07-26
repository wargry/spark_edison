'''
Twitter account configuration

name  : floodsgdl
email : floodsgdl@gmail.com

'''

import random
import twitter
from gmaps import Geocoding

gmaps_api = Geocoding()

twitter_api = twitter.Api(consumer_key='6JChZ7C9IHcAkfV3aiy5qwtTv',
                      consumer_secret='DdjiPc9ZNcXj8NQgX1Lsn9dJTC3UzLMzrqtwaZAO4lNpkGV9IH',
                      access_token_key='3295740896-EoaQrbFwPTZDUHU6csdeo96alHgz2xR0awft78a',
                      access_token_secret='hDJK1nqDFrXbkJD0bJ5prmzloIycQ6UBMUurE73MU1ygg')

def tweet(message):
    status = twitter_api.PostUpdate(message)

def get_place(Lat, Lon):
    query = gmaps_api.reverse(Lat, Lon)
    if not query:
       return 'somewhere'
    for component in query[0]['address_components']:
       if 'route' in component['types'] :
            return component['long_name']


def get_street(Lat, Lon):
    query = gmaps_api.reverse(Lat, Lon)
    if not query:
        return 'some street'
    for item in query:
	if 'street_address' in item['types']:
            return item['formatted_address']

def get_location(Lat, Lon):
    query = gmaps_api.reverse(Lat, Lon)
    if not query:
        return 'some place'
    for item in query:
        if 'sublocality_level_1' in item['types']:
            return item['formatted_address']
             
'''
# example
tweet('Floods GDL, Hello everyone!')
'''

def tweet_alert(alert, lat, lon):
    alerts = [
        tweet_place,
        tweet_street,
        tweet_location
    ]
    random.choice(alerts)(alert, lat, lon)

def tweet_place(alert, lat, lon):
    '''
    This function post an alert using the lat and long and converts to place
    '''
    tweet("{0} at {1}".format(alert, get_place(lat, lon)))

def tweet_street(alert, lat, lon):
    tweet("{0} in {1}".format(alert, get_street(lat,lon)))

def tweet_location(alert, lat, lon):
    tweet("{0}, {1}".format(alert, get_location(lat,lon)))

lat = 20.649470
lon = -103.402698

#print (get_place(lat,lon))
#print (get_street(lat,lon))
#print (get_location(lat,lon))
tweet_alert("Possible flood", lat, lon)
