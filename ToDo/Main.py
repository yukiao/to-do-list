from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import User
import sys
import Login as login

class Home(QWidget):
    def __init__(self):
        super(Home,self).__init__()
        self.setGeometry(200,200,400,200)
        self.initUi()
    
    def initUi(self):
        self.usernameLabel = QLabel('Username')
        self.usernameField = QLineEdit()
        self.passwordLabel = QLabel('Password')
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)

        self.button = QPushButton("Login")
        self.button.clicked.connect(self.onClicked)

        self.grid = QGridLayout()

        self.grid.addWidget(self.usernameLabel,0,0)
        self.grid.addWidget(self.usernameField,0,1)
        self.grid.addWidget(self.passwordLabel,1,0)
        self.grid.addWidget(self.passwordField,1,1)
        self.grid.addWidget(self.button,2,2)
        self.grid.setHorizontalSpacing(20)
        
        self.setLayout(self.grid)

    def onClicked(self):
        self.username = self.usernameField.text()
        self.password = self.passwordField.text()
        
        if login.Login().authentication(self.username,self.password):
            self.newWindow = User.User(self.username)
            self.newWindow.setWindowTitle("ToDoList")
            self.newWindow.show()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText('Wrong username/password')
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

def main():
    app = QApplication(sys.argv)
    win = Home()
    win.setWindowTitle("TodoList")
    win.show()
    sys.exit(app.exec_())

main()