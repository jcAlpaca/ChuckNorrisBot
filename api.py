import requests

chuckApiUrl = 'https://api.chucknorris.io/jokes/random'


def get_joke():
    try:
        apiUrlRequested = requests.get(chuckApiUrl)
        apiUrlJson = apiUrlRequested.json()
        joke = apiUrlJson['value']
        return joke
    except Exception as e:
        return 'Failed to get joke...'
