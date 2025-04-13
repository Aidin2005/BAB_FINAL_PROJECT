from PyQt5.QtWidgets import *
import pymysql as MySQLdb
from PyQt5.uic import loadUiType
from mainapp import MainApp

login,_ = loadUiType('login.ui')



class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='appuser' , password ='app123' , db='db')
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enterd Your Username And Password Correctly')

