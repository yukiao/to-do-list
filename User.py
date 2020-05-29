from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate
from os import path
from datetime import date
import UserInfo as userInfo
import datetime


class User(QWidget):
    def __init__(self, username):
        super(User, self).__init__()
        self.username = username
        self.path = 'User-Data/'+username+'.txt'
        self.initUi()

    def initUi(self):
        self.heading = QLabel('Hello '+userInfo.UserInfo().getAccount(self.username))
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.sort = QComboBox()
        self.sort.addItems(['Default','Status','Priority'])
        self.apply = QPushButton('Apply')
        self.apply.clicked.connect(self.applySort)
        
        self.title = QLabel('Events')
        self.title.setFont(QFont('Arial',16))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.data = []
        if(path.exists(self.path)):
            with open(self.path,'r') as rf:
                for line in rf:
                    if not(line in ('\n', '\r\n')):
                        self.data.append(line.split(";"))
        
        self.dataPane = QGridLayout()
        self.dataPane.setAlignment(QtCore.Qt.AlignHCenter)
        self.dataPane.setHorizontalSpacing(30)

        name = QLabel('Name')
        name.setFont(QFont('Arial', 12,10))
        name.setAlignment(QtCore.Qt.AlignCenter)

        desc = QLabel('Description')
        desc.setFont(QFont('Arial', 12,10))
        desc.setAlignment(QtCore.Qt.AlignCenter)

        for i in range(len(self.data)):
            self.dataPane.addWidget(name,0,0)
            self.dataPane.addWidget(desc,0,1)

            self.dataPane.addWidget(QLabel(self.data[i][0]),i+1,0)
            self.dataPane.addWidget(QLabel(self.data[i][3]),i+1,1)

        self.create = QPushButton('Create Event')
        self.create.clicked.connect(self.createEvent)
        self.delete = QPushButton('Delete Event')
        self.delete.clicked.connect(self.deleteItem)

        self.topHbox = QHBoxLayout()
        self.topHbox.addWidget(self.sort)
        self.topHbox.addWidget(self.apply)
        self.topHbox.setSpacing(30)

        self.bottomHbox = QHBoxLayout()
        self.bottomHbox.addWidget(self.create)
        self.bottomHbox.addWidget(self.delete)
        self.bottomHbox.setSpacing(10)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.heading)
        self.vbox.addLayout(self.topHbox)
        self.vbox.addWidget(self.title)
        self.vbox.addLayout(self.dataPane)
        self.vbox.addLayout(self.bottomHbox)
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.setSpacing(10)

        self.setLayout(self.vbox)

    def createEvent(self):
        self.window = QWidget()
        self.window.setWindowTitle('ToDoList')
        
        self.eventName = QLabel('Name')
        self.eventStart = QLabel('Start')
        self.eventEnd = QLabel('End')
        self.eventPriority = QLabel('Priority')
        self.eventDescription = QLabel('Description')
        self.submit = QPushButton('Submit')
        self.submit.clicked.connect(self.writeData)

        self.nameInput = QLineEdit()
        self.startInput = QDateEdit(calendarPopup=True)
        self.endInput = QDateEdit(calendarPopup=True)
        self.descriptionInput = QLineEdit()
        self.priorityInput = QComboBox()
        self.priorityInput.addItems(['High','Mid','Low'])

        self.gridPane = QGridLayout()
        self.gridPane.addWidget(self.eventName,0,0)
        self.gridPane.addWidget(self.nameInput,0,1)
        self.gridPane.addWidget(self.eventStart,1,0)
        self.gridPane.addWidget(self.startInput,1,1)
        self.gridPane.addWidget(self.eventEnd,2,0)
        self.gridPane.addWidget(self.endInput,2,1)
        self.gridPane.addWidget(self.eventDescription,3,0)
        self.gridPane.addWidget(self.descriptionInput,3,1)
        self.gridPane.addWidget(self.eventPriority,4,0)
        self.gridPane.addWidget(self.priorityInput,4,1)
        self.gridPane.addWidget(self.submit,5,1)

        self.window.setLayout(self.gridPane)
        self.window.show()
        self.close()

    def writeData(self):
        outputName = self.nameInput.text()
        start  = QDate(self.startInput.date())
        end = QDate(self.endInput.date())
        outputStart = start.toPyDate()
        outputEnd = end.toPyDate()
        outputDescription = self.descriptionInput.text()
        outputPriority = self.priorityInput.currentText()

        if(self.compareCalendar(outputStart,outputEnd)):
            if(outputName == ''):
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText('Event Name is null')
                msg.setIcon(QMessageBox.Critical)

                x = msg.exec_()
            else:
                if(not(path.exists(self.path))):
                    f = open(self.path,'w')
                    f.close()
                
                with open(self.path,'a') as wf:
                    wf.write('%s;%s;%s;%s;%s\n' %(outputName,outputStart,outputEnd,outputDescription,outputPriority))
                
                confirm = QMessageBox()
                confirm.setWindowTitle("Success")
                confirm.setText('Data Updated')
                confirm.setIcon(QMessageBox.Information)

                x = confirm.exec_()
                self.newWindow = User(self.username)
                self.newWindow.show()
                self.window.close()
        
        else:
            wrong = QMessageBox()
            wrong.setWindowTitle('Wrong')
            wrong.setText("Wrong date input")
            wrong.setIcon(QMessageBox.Critical)
            ex = wrong.exec_()

    def applySort(self):
        if(self.sort.currentText() == 'Default'):
            self.defaultList = []
            self.clearLayout(self.dataPane)
            if(path.exists(self.path)):
                with open(self.path,'r') as rf:
                    for line in rf:
                        if not(line in ('\n', '\r\n')):
                            self.defaultList.append(line.split(";"))
            name = QLabel('Name')
            name.setFont(QFont('Arial', 12,10))
            name.setAlignment(QtCore.Qt.AlignCenter)

            desc = QLabel('Description')
            desc.setFont(QFont('Arial', 12,10))
            desc.setAlignment(QtCore.Qt.AlignCenter)

            for i in range(len(self.data)):
                self.dataPane.addWidget(name,0,0)
                self.dataPane.addWidget(desc,0,1)

                self.dataPane.addWidget(QLabel(self.defaultList[i][0]),i+1,0)
                self.dataPane.addWidget(QLabel(self.defaultList[i][3]),i+1,1)

        elif(self.sort.currentText() == 'Priority'):
            self.defaultList = []
            self.clearLayout(self.dataPane)
            if(path.exists(self.path)):
                with open(self.path,'r') as hf:
                    for line in hf:
                        if not(line in ('\n', '\r\n')):
                            if 'High' in line:
                                self.defaultList.append(line.split(";"))

                with open(self.path,'r') as mf:
                    for line in mf:
                        if not(line in ('\n', '\r\n')):
                            if 'Mid' in line:
                                self.defaultList.append(line.split(";"))

                with open(self.path,'r') as lf:
                    for line in lf:
                        if not(line in ('\n', '\r\n')):
                            if 'Low' in line:
                                self.defaultList.append(line.split(";"))
            for i in range(len(self.defaultList)):
                name = QLabel('Name')
                name.setFont(QFont('Arial', 12,10))
                name.setAlignment(QtCore.Qt.AlignCenter)

                priority = QLabel('Priority')
                priority.setFont(QFont('Arial', 12,10))
                priority.setAlignment(QtCore.Qt.AlignCenter)
                
                self.dataPane.addWidget(name,0,0)
                self.dataPane.addWidget(priority,0,1)
                self.dataPane.addWidget(QLabel(self.defaultList[i][0]),i+1,0)
                self.dataPane.addWidget(QLabel(str(self.defaultList[i][4]).replace('\n','')),i+1,1)

        elif(self.sort.currentText() == 'Status'):
            self.defaultList = []
            self.clearLayout(self.dataPane)
            with open(self.path,'r') as rf:
                for line in rf:
                    if not(line in ('\n', '\r\n')):
                        self.defaultList.append(line.split(';'))
            if not(len(self.defaultList)==0):
                for i in range(len(self.defaultList)):
                    dateStart = list(map(int,self.defaultList[i][1].split('-')))
                    dateEnd = list(map(int,self.defaultList[i][2].split('-')))
                    
                    name = QLabel('Name')
                    name.setFont(QFont('Arial', 12,10))
                    name.setAlignment(QtCore.Qt.AlignCenter)

                    start = QLabel('Start')
                    start.setFont(QFont('Arial', 12,10))
                    start.setAlignment(QtCore.Qt.AlignCenter)

                    end = QLabel('End')
                    end.setFont(QFont('Arial', 12,10))
                    end.setAlignment(QtCore.Qt.AlignCenter)

                    status = QLabel('Status')
                    status.setFont(QFont('Arial', 12,10))
                    status.setAlignment(QtCore.Qt.AlignCenter)
 
                    self.dataPane.addWidget(name,0,0)
                    self.dataPane.addWidget(start,0,1)
                    self.dataPane.addWidget(end,0,2)
                    self.dataPane.addWidget(status,0,3)

                    self.dataPane.addWidget(QLabel(self.defaultList[i][0]),i+1,0)
                    self.dataPane.addWidget(QLabel(self.defaultList[i][1]),i+1,1)
                    self.dataPane.addWidget(QLabel(self.defaultList[i][2]),i+1,2)
                    self.dataPane.addWidget(QLabel(self.eventStatus(date.today(),date(dateStart[0],dateStart[1],dateStart[2]),date(dateEnd[0],dateEnd[1],dateEnd[2]))),i+1,3)
                

    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())

    def compareCalendar(self,start,end):
        if(start <= end):
            return True
        return False

    def eventStatus(self,today,start,end):
        if(today<start):
            return 'On going'
        if(today>end):
            return 'Finished'
        return 'Current'

    def deleteItem(self):
        self.layout = QWidget()
        self.defaultList = []

        if(path.exists(self.path)):
            with open(self.path,'r') as rf:
                for line in rf:
                    if not(line in ('\n', '\r\n')):
                        self.defaultList.append(line.split(";"))

        self.checkboxList = []
        for i in range(len(self.defaultList)):
            self.checkboxList.append(QCheckBox(self.defaultList[i][0]))
        
        self.vbox = QVBoxLayout()
        for i in range(len(self.checkboxList)):
            self.vbox.addWidget(self.checkboxList[i])
        self.vbox.addStretch(1)

        self.proceed = QPushButton('Delete')
        self.proceed.clicked.connect(self.deleteAction)
        self.vbox.addWidget(self.proceed)

        self.layout.setLayout(self.vbox)
        self.layout.show()
        self.close()

    def deleteAction(self):
        selectedItem = []
        newFile = []
        for i in range(len(self.checkboxList)):
            self.checkedItem = self.checkboxList[i]
            if(self.checkedItem.isChecked()):
                selectedItem.append(self.checkedItem.text())
        
        with open (self.path, 'r') as rf:
            for line in rf:
                if not(line.split(';')[0] in selectedItem):
                    newFile.append(line)
        
        with open(self.path, 'w') as wf:
            for line in newFile:
                wf.write(line)
            wf.write('\n')

        confirm = QMessageBox()
        confirm.setWindowTitle("Success")
        confirm.setText('Event Deleted')
        confirm.setIcon(QMessageBox.Information)

        execute = confirm.exec_()

        self.openWindow = User(self.username)
        self.openWindow.show()
        self.layout.close()
