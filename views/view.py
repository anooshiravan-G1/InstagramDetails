# view.py
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox, QLineEdit, QDialog, QLabel

from controller.controller import InstaLoaderController


class CustomInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Write your ID here")
        self.setStyleSheet("background-color: white; color: black;")

        layout = QVBoxLayout(self)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

    def getText(self):
        return self.input_field.text()


def display_message(message_text, messageTitle):
    msgBox = QMessageBox()
    msgBox.setStyleSheet("QMessageBox {background-color: white;}")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message_text)
    msgBox.setWindowTitle(messageTitle)
    msgBox.exec_()



class InstaLoaderView(QWidget):
    def __init__(self):
        super().__init__()

        #Controller
        self.controller = InstaLoaderController()

        #window Visuals
        self.setWindowTitle("InstaLoader")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #23242a;")
        self.setWindowTitle("InstaLoader")

        # Layout
        self.layout = QVBoxLayout()

        
        # Buttons
        self.download_pic_button = QPushButton("Download Profile Picture", self)
        self.download_posts_button = QPushButton("Download All Posts", self)
        self.download_bio_button = QPushButton("Download Bio", self)
        self.save_followings_button = QPushButton("Save Followings", self)
        self.exit_button = QPushButton("Exit", self)
        
        # Add buttons to layout
        self.layout.addWidget(self.download_pic_button)
        self.layout.addWidget(self.download_posts_button)
        self.layout.addWidget(self.download_bio_button)
        self.layout.addWidget(self.save_followings_button)
        self.layout.addWidget(self.exit_button)



        # Set button width to capture half of the window
        button_width = self.width() 
        button_height = self.height() / 4
        self.download_pic_button.setFixedSize(button_width, button_height)
        self.download_posts_button.setFixedSize(button_width, button_height)
        self.download_bio_button.setFixedSize(button_width, button_height)
        self.save_followings_button.setFixedSize(button_width, button_height)
        self.exit_button.setFixedSize(button_width, button_height)

        # Align buttons to the left
        self.layout.addWidget(self.download_pic_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.download_posts_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.download_bio_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.save_followings_button, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.exit_button, alignment=Qt.AlignCenter)

        # Set layout
        self.setLayout(self.layout)


        # Button Visuals
        radius = 10
        self.download_pic_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                               "QPushButton:hover { background-color: grey; }" % radius )
        self.download_posts_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                                 "QPushButton:hover { background-color: grey; }" % radius )
        self.download_bio_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                                 "QPushButton:hover { background-color: grey; }" % radius )
        self.save_followings_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                                 "QPushButton:hover { background-color: grey; }" % radius )
        self.exit_button.setStyleSheet("QPushButton { background-color: white; color: black; border: 2px solid white; border-radius: %dpx; font-size: 14px; }"
                                       "QPushButton:hover { background-color: grey; }" % radius )


        self.download_pic_button.clicked.connect(self.download_profile_pic)
        self.download_posts_button.clicked.connect(self.download_all_posts)
        self.download_bio_button.clicked.connect(self.download_bio)
        self.save_followings_button.clicked.connect(self.save_followings)
        self.exit_button.clicked.connect(self.close)


    
    def download_profile_pic(self):
        custom_dialog = CustomInputDialog(self)
        if custom_dialog.exec_() == QDialog.Accepted:
            text = custom_dialog.getText()
            if text:
                self.controller.download_profile_pic(text)


    def download_all_posts(self):

        custom_dialog = CustomInputDialog(self)
        if custom_dialog.exec_() == QDialog.Accepted:
            text = custom_dialog.getText()
            if text:
                self.controller.download_all_posts(text)


    def download_bio(self):

        custom_dialog = CustomInputDialog(self)
        if custom_dialog.exec_() == QDialog.Accepted:
            text = custom_dialog.getText()
            if text:
                bio = self.controller.download_bio(text)
                #QMessageBox.information(self, "Bio", bio)
                display_message(bio, "Bio")


    def save_followings(self):
      dialog = CustomInputDialog()
      ok = dialog.exec_()
      username_story_page = dialog.getText()[0] if ok else None

      if username_story_page:
        self.controller.save_followings_to_file(username_story_page)
