
import json
import time


def read_token():
    with open('env.json', 'r') as env:
        return json.load(env)

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

    with open('env.json', 'a') as env:
        json.dump(token_data, env)


write_token("test")
