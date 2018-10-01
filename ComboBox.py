import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItems(["SublimeText","VsCode","Gedit","Atom"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
      
      #layout.addStretch()	
      layout.addWidget(self.cb)

      self.cb.currentIndexChanged.connect(self.selectionchange)

      self.setLayout(layout)

      self.setWindowTitle("Select your Text Editor")
      self.setGeometry(10,10,300,200)

   def selectionchange(self,i):

       print("selcetionText is "+self.cb.currentText())
       select_text = self.cb.currentText()

def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()