import requests
import json


def get_users_list(url):
    return requests.get(url)