import requests

BASE_URL = 'https;//apis.paralleldots.com/'

API_KEY = '21daclczqmKNKHZDfXyUqpyUr1i98ecvffCJD7KDb4s'

input = raw_input('Enter Text')

request_url = BASE_URL + 'sentiment?sentence1=%s&apikey=%s' % (input, API_KEY)
response = requests.get(request_url, verify=False).json()
print response
