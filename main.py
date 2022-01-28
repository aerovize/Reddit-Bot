import time
import data
from api import *


def authenticate():
    token = data.get_token()
    data.write_token(token)


def token():
    auth_token = data.read_token()
    auth_token = auth_token["token"]
    return auth_token


def create_post(token):
    title = "Whats up"
    text = "Sorry I got bored"
    sr = "aerot3st"
    submit_post(title, text, sr, token)


def main():
    # temporary list for storing new posts
    temp = []

    # get the previous count of posts & the newest post's reddit id (starts with t3_)
    mem = data.get_memory()

    # assign the previous count to variable
    prev_count = mem["count"]

    # needs to be a int
    prev_count = int(prev_count)

    # get the auth token we have stored
    auth_token = token()
    # check to see if the token expired, otherwise move along
    expired = data.is_expired()
    if expired:
        print("------REAUTHENTICATING------")
        authenticate()

    # get all posts from the subreddit
    all_posts = get_posts(auth_token)

    # check to see if the id we have stored matches the most recent post
    # in the subreddit, because theres no reason to continue.
    if mem["last_id"] != all_posts[0]:
        # assign the current count to the length of all posts currently on the subreddit
        curr_count = len(all_posts)

        # check to see if the current amount of posts on the subreddit is a larger number,
        # because if so we can be positive that there is a new post
        if curr_count > prev_count:
            # new_count is the amount of new posts there are
            new_count = curr_count - prev_count
            # Loop through all of the posts based upon the index and
            # if it is one of the new ones add it to out [temp] list
            for i in all_posts:
                if all_posts.index(i) <= new_count:
                    temp.append(i)

            # update our previous post count and the id of the most recent post into our db
            data.set_memory(len(all_posts), temp[0])

            # make sure the bot comments on the new posts
            for post in temp:
                comment(auth_token, "Groovy", post)
        print("Time to sleep")
        # sleep then go back to work
        time.sleep(10)
        main()

    else:
        # if there has been no new posts added then things are boring, so we will
        # add a new post
        print("Im getting bored")
        create_post(auth_token)
        time.sleep(10)
        main()


if __name__ == '__main__':

    main()
