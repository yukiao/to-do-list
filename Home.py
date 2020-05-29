from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import Login as login
import User
import Account as account

class Home(QWidget):
    def __init__(self):
        super(Home,self).__init__()
        self.setContentsMargins(20,20,20,20)
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

        self.create = QPushButton("Create Account")
        self.create.clicked.connect(self.createAccount)

        self.grid.addWidget(self.usernameLabel,0,0)
        self.grid.addWidget(self.usernameField,0,1)
        self.grid.addWidget(self.passwordLabel,1,0)
        self.grid.addWidget(self.passwordField,1,1)
        self.grid.addWidget(self.button,2,2)
        self.grid.addWidget(self.create,3,2)
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

    def createAccount(self):
        self.createNewAccount = account.Account()
        self.createNewAccount.show()
        self.close()
