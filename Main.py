from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import Home 
import sys

def main():
    app = QApplication(sys.argv)
    win = Home.Home()
    win.setWindowTitle("TodoList")
    win.show()
    sys.exit(app.exec_())

main()