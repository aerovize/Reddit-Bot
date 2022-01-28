import requests

# Handles get requests


def get_api(auth_token, params):
    headers = {"Authorization": f"bearer {auth_token}",
               "User-Agent": "Aerobot/0.1 by aeromaniacus"}
    response = requests.get(
        f"https://oauth.reddit.com/{params}", headers=headers)
    return response.json()

# Handles post requests


def post_api(auth_token, path, body):
    headers = {
        "User-Agent": "Aerobot/0.1 by aeromaniacus",
        "Authorization": f"bearer {auth_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(
        f"https://oauth.reddit.com/{path}", headers=headers, data=body)

    return response.json()

# Submits a new post to a subreddit


def submit_post(title, text, sr, auth_token):
    path = "api/submit"
    body = {
        "title": title,
        "text": text,
        "sr": sr,
        "kind": "self",
        "resubmit": "true",
        "send_replies": "true"
    }
    post_api(auth_token, path, body)


def comment(auth_token, text, id):
    path = "api/comment"
    body = {
        "text": text,
        "thing_id": id
    }
    post_api(auth_token, path, body)


def get_posts(auth_token):
    post_ids = []
    params = "r/aerot3st/new"
    resp = get_api(auth_token, params)
    data = resp["data"]["children"]

    for post in data:
        post = post["data"]["name"]
        post_ids.append(post)

    return post_ids
