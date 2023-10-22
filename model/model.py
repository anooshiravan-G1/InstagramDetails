# model.py
import instaloader

class InstaLoaderModel:
    def __init__(self):
        self.L = instaloader.Instaloader()

    def download_profile_pic(self, username):
        profile = instaloader.Profile.from_username(self.L.context, username)
        self.L.download_profilepic(profile)

    def download_all_posts(self, username):
        profile = instaloader.Profile.from_username(self.L.context, username)
        for post in profile.get_posts():
            self.L.download_post(post, target=profile.username)
