import requests
import secrets

nyt_key = 'ce642fbdc5234cbb9a549483edf4af2f'

# gets stories from a particular section of NY times
#constructing our query
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/' #from NYT documentation
    extendedurl = baseurl + section + '.json'
    params={'api-key': secrets.nyt_key}
    return requests.get(extendedurl, params).json()

section = 'science'
stories = get_stories(section)
print(stories) # should print a big pile of json
