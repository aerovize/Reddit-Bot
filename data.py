import requests
import requests.auth
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Uses reddits simple oauth flow


def get_token():
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    CLIENT = os.getenv("CLIENT")
    SECRET = os.getenv("SECRET")

    client_auth = requests.auth.HTTPBasicAuth(
        CLIENT, SECRET)

    post_data = {"grant_type": "password",
                 "username": USERNAME, "password": PASSWORD, "scope": "submit,read"}

    headers = {"User-Agent": "Aerobot/0.1 by aeromaniacus"}

    response = requests.post("https://www.reddit.com/api/v1/access_token",
                             auth=client_auth, data=post_data, headers=headers)
    auth_data = response.json()

    return auth_data['access_token']

# Reads a JSON file that is used to store the auth token and timestamp


def read_token():
    with open('db.json', 'r') as db:
        return json.load(db)

# check to see if the token has expired, token has a 1 hour lifespan


def is_expired():
    token = read_token()
    if time.time() >= token["expire"]:
        return True

# writes auth token to the JSON file along with a timestamp for when the token expires


def write_token(token):
    token_data = {
        "token": token,
        "expire": time.time() + 3600}

    with open('db.json', 'w') as db:
        json.dump(token_data, db)


def set_memory(count, id):
    previous = {
        "count": count,
        "last_id": id
    }
    with open('memory.json', 'w') as mem:
        json.dump(previous, mem)


def get_memory():
    with open('memory.json', 'r') as mem:
        return json.load(mem)
