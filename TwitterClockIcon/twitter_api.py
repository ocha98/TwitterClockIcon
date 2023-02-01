import tweepy

class UpdateProfileIcon:
    def __init__(self,
                API_KEY,
                API_KEY_SECRET,
                ACCESS_TOKEN,
                ACCESS_TOKEN_SECRET
                ):

        auth = tweepy.OAuth1UserHandler(
            API_KEY,
            API_KEY_SECRET,
            ACCESS_TOKEN,
            ACCESS_TOKEN_SECRET,
            )
        self.api = tweepy.API(auth)

    def update_profile_icon(self, img_path):
        self.api.update_profile_image(img_path)
