from PyQt5.QtWidgets import *
import sys
from mainapp import MainApp
from login import Login

def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()