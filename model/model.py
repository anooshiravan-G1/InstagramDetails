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

    def download_bio(self, username):
        profile = instaloader.Profile.from_username(self.L.context, username)
        return profile.biography
    
    def get_followings(self, username):
        profile = instaloader.Profile.from_username(self.L.context, username)
        followings = [following.username for following in profile.get_followees()]
        return followings
