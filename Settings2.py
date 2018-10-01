import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

def window():
   app = QApplication(sys.argv)
   win = QWidget()

   l1 = QLabel(" Duration of record ")
   nm = QLineEdit()
   fbox = QFormLayout()
   fbox.addRow(l1,nm)
   fuu=QPushButton("Submit")
   fbox.addRow(fuu,QPushButton("Cancel"))
   fuu.clicked.connect(showMeHow)

   win.setLayout(fbox)
   
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())
def showMeHow():
    cmd="python ComboBox.py"
    os.system(cmd) 
if __name__ == '__main__':
   window()