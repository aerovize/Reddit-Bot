import time
import auth
import endpoint as ep


def authenticate():
    token = auth.get_token()
    auth.write_token(token)


def token():
    auth_token = auth.read_token()
    auth_token = auth_token["token"]
    return auth_token


def create_post():
    title = "lol"
    text = "bbbbbbb"
    sr = "aerot3st"

    ep.submit_post(title, text, sr, token())


def main(t, pc):
    prev_count = 3
    temp = []
    auth_token = token()
    # check to see if the token expired, otherwise move along
    expired = auth.is_expired()
    if expired:
        print("------REAUTHENTICATING------")
        authenticate()
    all_posts = ep.get_posts(auth_token)

    if all_posts[0] != temp[0]:
        curr_count = len(all_posts)
        if curr_count > prev_count:
            new_count = curr_count - prev_count

        for i in all_posts:
            if all_posts.index(i) <= new_count:
                temp.append(i)

        for post in temp:
            ep.comment(auth_token, "Groovy", post)
        # time.sleep(10)
        # main()


if __name__ == '__main__':

    main()
