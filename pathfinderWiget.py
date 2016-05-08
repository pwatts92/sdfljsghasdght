'''
Created on Apr 4, 2016

@author: parker
'''

from PyQt4 import QtGui
from PyQt4.QtGui import QHBoxLayout, QPalette, QBrush, QPixmap
from Main.rpgClass import *
from Main.rpgCharacter import *

 
class BasicWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(BasicWidget, self).__init__(parent)   
                      
        self.h_layout = QHBoxLayout()
        self.setStyleSheet('font-size: 14pt; font-family: Times;')
        self.setGeometry(500, 500, 500, 500)
                
        # Set Window text and wigets
        genButton = QtGui.QPushButton("Generate Character", self)
        genButton.clicked.connect(self.generateCharacter(self))
        genButton.resize(genButton.minimumSizeHint())
        genButton.move(0,100)
        
        classLabel = QtGui.QLabel("Class")
        classBox = QtGui.QComboBox(self)
        classBox.addItem("Fighter")
        classBox.addItem("Rogue")
        #classBox.addItems("Fighter", "Rogue", "Cleric", "Wizard")
        
        statGenLabel = QtGui.QLabel("Stat Type")
        statGenBox = QtGui.QComboBox(self)
        statGenBox.addItem("Normal")
        statGenBox.addItem("Minion")
        statGenBox.addItem("Mighty")
        
        nameLabel = QtGui.QLabel("Name")
        nameField = QtGui.QLineEdit()
        
        '''FIX THIS SHIT
        if (classBox.currentText() == "Fighter"):
            #characterClass = Fighter()
            #character = rpgCharacter.RPGCharacter(Fighter(), 1)
            character = RPGCharacter(Fighter(), 1)
            characterClass = character.RPGClass
        
        #nameField.setText(str(characterClass.attackBonus(character.level)))
        nameField.setText(str(characterClass.attackBonus(1)))'''
        
        #Put GUI elements in the widget
        mainLayout = QtGui.QGridLayout()
        
        mainLayout.addWidget(nameLabel, 498, 0)
        mainLayout.addWidget(nameField, 499, 0)
        
        mainLayout.addWidget(classLabel, 0, 0)
        mainLayout.addWidget(classBox, 1, 0)
        
        mainLayout.addWidget(statGenLabel, 0, 0)
        mainLayout.addWidget(statGenBox, 0, 0)
        
        # Window and Background configuration
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("oldpaper.jpg")))
    
        self.setPalette(palette)
        self.setLayout(mainLayout)
        self.setWindowTitle("Pathfinder Character Generator")
        
    def generateCharacter(self, momWidget):
        if (momWidget.classBox.currentText() == "Fighter"):
            #characterClass = Fighter()
            #character = rpgCharacter.RPGCharacter(Fighter(), 1)
            character = RPGCharacter(Fighter(), 1)
            characterClass = character.RPGClass
        
        #nameField.setText(str(characterClass.attackBonus(character.level)))
        momWidget.nameField.setText(str(characterClass.attackBonus(1)))
        #widgetCharacter = RPGCharacter(self, self.characterClass, 1)
 
if __name__ == '__main__':
    import sys
 
    app = QtGui.QApplication(sys.argv)
 
    helloPythonWidget = BasicWidget()
    helloPythonWidget.show()
 
    sys.exit(app.exec_())
    
