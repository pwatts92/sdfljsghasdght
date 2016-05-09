import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(lambda: self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
      
class Example2(QtGui.QWidget):
    
    def __init__(self):
        super(Example2, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        lbl1 = QtGui.QLabel('ZetCode', self)
        lbl1.move(15, 10)

        lbl2 = QtGui.QLabel('tutorials', self)
        lbl2.move(35, 40)
        
        lbl3 = QtGui.QLabel('for programmers', self)
        lbl3.move(55, 70)        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
