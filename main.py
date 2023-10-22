# main.py
import sys
from PyQt5.QtWidgets import QApplication
from views.view import InstaLoaderView

def main():
    app = QApplication(sys.argv)
    view = InstaLoaderView()
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()