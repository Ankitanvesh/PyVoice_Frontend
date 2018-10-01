import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

class menudemo(QMainWindow):
   def __init__(self, parent = None):
      super(menudemo, self).__init__(parent)
		
      layout = QHBoxLayout()
      bar = self.menuBar()
      file = bar.addMenu("File")
      settings = QAction("Settings",self)
      settings.setShortcut("Ctrl+Alt+v")
      file.addAction(settings)
		
      file.triggered[QAction].connect(self.processtrigger)
      self.setLayout(layout)
      self.setWindowTitle("menu demo")
		
   def processtrigger(self,q):
         if q.text()=="Settings":

               cmd="python Settings2.py"
               os.system(cmd)
      
		
def main():
   app = QApplication(sys.argv)
   ex = menudemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()