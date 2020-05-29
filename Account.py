from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import Home as home

class Account(QWidget):
    def __init__(self):
        super(Account,self).__init__()
        self.initUi()
    def initUi(self):
        self.labelName = QLabel('Name')
        self.labelUser = QLabel('Username')
        self.labelPassword = QLabel('Password')
        self.nameField = QLineEdit()
        self.userField = QLineEdit()
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create = QPushButton('Submit')
        self.create.clicked.connect(self.submitAction)

        self.grid = QGridLayout()
        self.grid.addWidget(self.labelName,0,0)
        self.grid.addWidget(self.nameField,0,1)
        self.grid.addWidget(self.labelUser,1,0)
        self.grid.addWidget(self.userField,1,1)
        self.grid.addWidget(self.labelPassword,2,0)
        self.grid.addWidget(self.passwordField,2,1)
        self.grid.addWidget(self.create,3,0)

        self.setLayout(self.grid)

    def submitAction(self):
        with open ('Account.txt','a') as wf:
            wf.write('\n%s;%s' %(self.userField.text(),self.passwordField.text()))
        
        with open ('UserInfo.txt','a') as af:
            af.write('\n%s;%s' %(self.userField.text(),self.nameField.text()))

        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText('Account Added')
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

        self.openHome = home.Home()
        self.openHome.show()
        self.close()