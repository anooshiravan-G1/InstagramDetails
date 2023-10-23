# view.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox, QLineEdit

from controller.controller import InstaLoaderController

class InstaLoaderView(QWidget):
    def __init__(self):
        super().__init__()

        #Controller
        self.controller = InstaLoaderController()

        #window Visuals
        self.setWindowTitle("InstaLoader")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #23242a;")
        self.setWindowTitle("InstaLoader")
        self.layout = QVBoxLayout()
        
        
        self.download_pic_button = QPushButton("Download Profile Picture", self)
        self.download_posts_button = QPushButton("Download All Posts", self)
        self.download_stories_button = QPushButton("Download Stories", self)
        self.download_bio_button = QPushButton("Download Bio", self)
        self.exit_button = QPushButton("Exit", self)
        
        self.layout.addWidget(self.download_pic_button)
        self.layout.addWidget(self.download_posts_button)
        self.layout.addWidget(self.download_stories_button)
        self.layout.addWidget(self.download_bio_button)
        self.layout.addWidget(self.exit_button)
        


        # Set button width to capture half of the window
        button_width = self.width() / 2
        button_height = self.height() / 12
        self.download_pic_button.setFixedSize(button_width, button_height)
        self.download_posts_button.setFixedSize(button_width, button_height)
        self.download_stories_button.setFixedSize(button_width, button_height)
        self.download_bio_button.setFixedSize(button_width, button_height)
        self.exit_button.setFixedSize(button_width, button_height)

        # Align buttons to the left
        self.layout.addWidget(self.download_pic_button, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.download_posts_button, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.download_stories_button, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.download_bio_button, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.exit_button, alignment=Qt.AlignLeft)

        self.setLayout(self.layout)


        # Button Visuals
        radius = 10
        self.download_pic_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                               "QPushButton:hover { background-color: grey; }" % radius )
        self.download_posts_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                                 "QPushButton:hover { background-color: grey; }" % radius )
        self.download_stories_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                               "QPushButton:hover { background-color: grey; }" % radius )
        self.download_bio_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                                 "QPushButton:hover { background-color: grey; }" % radius )
        self.exit_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                       "QPushButton:hover { background-color: grey; }" % radius )


        self.download_pic_button.clicked.connect(self.download_profile_pic)
        self.download_posts_button.clicked.connect(self.download_all_posts)
        self.download_stories_button.clicked.connect(self.download_stories)
        self.download_bio_button.clicked.connect(self.download_bio)
        self.exit_button.clicked.connect(self.close)

    def download_profile_pic(self):
        style_sheet = (
            "QLineEdit { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
            "QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
        )
        text.setStyleSheet(style_sheet)
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your Instagram ID:', QLineEdit.Normal, '', flags=Qt.CustomizeWindowHint)
        
        if ok:
            self.controller.download_profile_pic(text)

    def download_all_posts(self):
        style_sheet = (
            "QLineEdit { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
            "QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
        )
        text.setStyleSheet(style_sheet)
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your Instagram ID:', QLineEdit.Normal, '', flags=Qt.CustomizeWindowHint)
        
        if ok:
            self.controller.download_all_posts(text)
    
    def download_stories(self):
        style_sheet = (
            "QLineEdit { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
            "QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
        )
        text.setStyleSheet(style_sheet)
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your Instagram ID:', QLineEdit.Normal, '', flags=Qt.CustomizeWindowHint)
        
        if ok:
            self.controller.download_stories(text)

    def download_bio(self):
        style_sheet = (
            "QLineEdit { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
            "QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: 5px; }"
        )
        text.setStyleSheet(style_sheet)
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your Instagram ID:', QLineEdit.Normal, '', flags=Qt.CustomizeWindowHint)
        
        if ok:
            bio = self.controller.download_bio(text)
            QMessageBox.information(self, "Bio", bio)