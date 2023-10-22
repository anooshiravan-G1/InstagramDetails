# view.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog
from controller.controller import InstaLoaderController

class InstaLoaderView(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = InstaLoaderController()
        self.setWindowTitle("InstaLoader")
        self.layout = QVBoxLayout()
        
        self.download_pic_button = QPushButton("Download Profile Picture")
        self.download_posts_button = QPushButton("Download All Posts")
        self.exit_button = QPushButton("Exit")
        
        self.layout.addWidget(self.download_pic_button)
        self.layout.addWidget(self.download_posts_button)
        self.layout.addWidget(self.exit_button)
        
        self.setLayout(self.layout)

        self.download_pic_button.clicked.connect(self.download_profile_pic)
        self.download_posts_button.clicked.connect(self.download_all_posts)
        self.exit_button.clicked.connect(self.close)

    def download_profile_pic(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your Instagram ID:')
        
        if ok:
            self.controller.download_profile_pic(text)

    def download_all_posts(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your Instagram ID:')
        
        if ok:
            self.controller.download_all_posts(text)