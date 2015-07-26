'''
Twitter account configuration

name  : floodsgdl
email : floodsgdl@gmail.com

'''

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
    #print(gmaps_api.reverse(Lat, Lon))
    query = gmaps_api.reverse(Lat, Lon)

    #print (query[0]['address_components'][1]['long_name'])
    if not query:
       return 'somewhere'
    for component in query[0]['address_components']:
       if 'route' in component['types'] :
            return component['long_name']
         
'''
# example
tweet('Floods GDL, Hello everyone!')
'''

def tweet_location(message, lat, lon):
    '''
    This function post a message using the lat and long and converts to place
    '''
    tweet("{0} at {1}".format(message, get_place(lat, lon)))

lat = 20.649470
lon = -103.402698

# print (get_place(lat,lon))
tweet_location("Flood detection", lat, lon)
