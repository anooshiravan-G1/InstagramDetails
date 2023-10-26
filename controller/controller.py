# controller.py
from model.model import InstaLoaderModel

class InstaLoaderController:
    def __init__(self):
        self.model = InstaLoaderModel()

    def download_profile_pic(self, username):
        self.model.download_profile_pic(username)

    def download_all_posts(self, username):
        self.model.download_all_posts(username)

    def download_bio(self, username):
        return self.model.download_bio(username)
    
    def save_followings_to_file(self, username):
        followings = self.model.get_followings(username)
        with open('followings.txt', 'w') as f:
            for following in followings:
                f.write(following + '\n')
