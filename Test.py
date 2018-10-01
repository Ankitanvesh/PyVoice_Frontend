import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
import os

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
		
      layout = QVBoxLayout()
        
      self.buttone = QPushButton("Settings")
      self.buttone.clicked.connect(self.processtrigger)
      layout.addWidget(self.buttone)
      self.btn = QPushButton("   Choose a python file you would like to edit    ")
      self.btn.clicked.connect(self.getfile)
		
      
      layout.addWidget(self.btn)
      self.le = QLabel()
      self.le.setPixmap(QPixmap("Kira.jpeg"))
	  
      layout.addStretch()	
      layout.addWidget(self.le)
      self.btn1 = QLabel("Create a new Python file (Press Enter when done)")
      
      self.bb = QLineEdit()
      layout.addStretch() 
      layout.addWidget(self.btn1)
      layout.addWidget(self.bb)
      
      self.bb.returnPressed.connect(self.textfucker)
      
      
      self.button=QPushButton("Start")

      layout.addWidget(self.button)
      self.pbar = QtGui.QProgressBar(self)
      self.button.clicked.connect(self.showdialog)
      
      

      self.setLayout(layout)
      self.setWindowTitle(" PyAudio ")
      self.setGeometry(100,100,500,400)
		
   def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Text files (*.py)")
      
      if os.stat(fname).st_size >= 0:
        cmd="code %s"%(fname)
        os.system(cmd)
		
   def textfucker(self):
       print(self.bb.text())
       filename = self.bb.text()+".py"
       cmd= "touch %s"%(filename)
       os.system(cmd) 
       if len(self.bb.text()) > 0:
           comd="code %s"%(filename)
           os.system(comd)

   def selectionchange(self):
       print("selcetionText is "+self.cb.currentText())
       select_text = self.cb.currentText()


   def showdialog(self):
       cmd="python Progress.py"
       os.system(cmd)


   def processtrigger(self,q):
         cmd="python Settings2.py"
         os.system(cmd)    
         

             
                
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()