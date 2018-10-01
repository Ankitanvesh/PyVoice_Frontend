import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
import os

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("   Choose a python file you would like to edit    ")
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.le = QLabel()
      self.le.setPixmap(QPixmap("Kira.jpeg"))
		
      layout.addWidget(self.le)
      self.btn1 = QLabel("Create a new Python file (Press Enter when done)")
      
      self.bb = QLineEdit()
      layout.addStretch() 
      layout.addWidget(self.btn1)
      layout.addWidget(self.bb)
      
      self.bb.returnPressed.connect(self.textfucker)
      self.cb = QComboBox()
      self.cb.addItems(["SublimeText","VsCode","Gedit","Atom"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
      layout.addStretch()	
      layout.addWidget(self.cb)

      #layouthor = QHBoxLayout()
      
      self.button=QPushButton("Start")

      layout.addWidget(self.button)
      self.pbar = QtGui.QProgressBar(self)
      self.pbar.setGeometry(30, 40, 200, 25)
      #self.b222.clicked.connect(self.doAction)
      self.btn = QtGui.QPushButton('Start', self)
      self.btn.move(40, 80)
      self.button.clicked.connect(self.showdialog)
      #layout.addWidget(self.pbar)
      self.timer = QtCore.QBasicTimer()
      self.step = 0
      

      self.setLayout(layout)
      self.setWindowTitle("File Dialog demo")
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


   def timerEvent(self, e):
      
       if self.step >= 100:
       
           self.timer.stop()
           self.btn.setText('Finished')
           return
           
       self.step = self.step + 1
       self.pbar.setValue(self.step)

   def doAction(self):
      
       if self.timer.isActive():
           self.timer.stop()
           self.btn.setText('Start')
           
       else:
           self.timer.start(50, self)
           self.btn.setText('Stop')


   def showdialog(self):
       d = QDialog()
       self.pbar = QtGui.QProgressBar()
       self.pbar.setGeometry(30, 40, 200, 25)   
       self.btn = QtGui.QPushButton('Start',d)
       self.btn.move(40, 80)
       self.btn.clicked.connect(self.doAction)   
       self.timer = QtCore.QBasicTimer()
       self.step = 0
       
       d.setGeometry(300, 300, 280, 170)
       d.setWindowTitle('QtGui.QProgressBar')
       d.exec_()

                
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()