# pip install pyqt5
# pip install pyqt5 pyqt5-tools


import sys
from PyQt5.QtWidgets import *           # imports section

app = QApplication(sys.argv)            # create application
dlgMain = QWidget()                     # create main GUI canvas
dlgMain.setWindowTitle("My GUI")
dlgMain.show()                          # show the GUI

app.exec_()