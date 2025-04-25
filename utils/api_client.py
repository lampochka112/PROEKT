import requests
from config import API_URL

def fetch_news():
    response = requests.get(API_URL)
    return response.json()