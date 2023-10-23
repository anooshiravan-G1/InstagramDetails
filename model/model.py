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
    
    def download_stories(self, username):
        profile = instaloader.Profile.from_username(self.L.context, username)
        for story in self.L.get_stories_userids([profile.userid]):
            for item in story.get_items():
                self.L.download_storyitem(item, ':stories')

    def download_bio(self, username):
        profile = instaloader.Profile.from_username(self.L.context, username)
        return profile.biography
