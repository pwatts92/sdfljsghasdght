'''
Created on Apr 4, 2016

@author: parker
'''

from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Main.rpgClass import *
from Main.rpgCharacter import *

 
class BasicWidget(QtGui.QWidget):
    def __init__(self):
        super(BasicWidget, self).__init__()   
                 
        self.h_layout = QHBoxLayout()
        self.setStyleSheet('font-size: 14pt; font-family: Times;')
        self.setGeometry(0, 0, 1000, 1000)
        #self.statusBar()
        #self.center()
                
        # Set Window text and wigets
        classLabel = QtGui.QLabel("Class", self)
        self.classBox = QtGui.QComboBox(self)
        classList = ("Random", "Random Warrior", "Random Spellcaster", "Fighter", "Rogue", "Ranger", "Wizard", "Cleric")
        self.classBox.addItems(classList)
        classLabel.move(25,5)
        self.classBox.move(75,5)
        
        levelLabel = QtGui.QLabel("Level", self)
        self.levelBox = QtGui.QComboBox(self)
        levelList = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
        self.levelBox.addItems(levelList)
        levelLabel.move(240,5)
        self.levelBox.move(300,5)
        
        statGenLabel = QtGui.QLabel("Stat Type", self)
        self.statGenBox = QtGui.QComboBox(self)
        self.statGenBox.addItem("Normal")
        self.statGenBox.addItem("Minion")
        self.statGenBox.addItem("Mighty")
        statGenLabel.move(440, 5)
        self.statGenBox.move(525,5)
        
        strLabel = QtGui.QLabel("STR", self)
        strLabel.move(25, 100)
        dexLabel = QtGui.QLabel("DEX", self)
        dexLabel.move(25, 150)
        conLabel = QtGui.QLabel("CON", self)
        conLabel.move(25, 200)
        intLabel = QtGui.QLabel("INT", self)
        intLabel.move(25, 250)
        wisLabel = QtGui.QLabel("WIS", self)
        wisLabel.move(25, 300)
        chaLabel = QtGui.QLabel("CHA", self)
        chaLabel.move(25, 350)
        
        self.strBox = QtGui.QTextEdit(self)
        self.strBox.move(75, 100)
        self.dexBox = QtGui.QTextEdit(self)
        self.dexBox.move(75, 150)
        self.conBox = QtGui.QTextEdit(self)
        self.conBox.move(75, 200)
        self.intBox = QtGui.QTextEdit(self)
        self.intBox.move(75, 250)
        self.wisBox = QtGui.QTextEdit(self)
        self.wisBox.move(75, 300)
        self.chaBox = QtGui.QTextEdit(self)
        self.chaBox.move(75, 350)
        
        genButton = QtGui.QPushButton("Generate Character", self)
        genButton.clicked.connect(lambda: self.generateCharacter())
        genButton.resize(genButton.minimumSizeHint())
        genButton.move(400,50)
        
        #Put GUI elements in the widget
        mainLayout = QtGui.QGridLayout()
        
        # Window and Background configuration
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("oldpaper.jpg")))
    
        self.setPalette(palette)
        self.setLayout(mainLayout)
        self.setWindowTitle("Pathfinder Character Generator")
        
    def generateCharacter(self):
        #classText = self.classBox.currentText()
        if (self.classBox.currentText() == "Random"):
            randomInt = random.randrange(1, 5)
            if(randomInt == 1):
                character = RPGCharacter(Fighter(), int(self.levelBox.currentIndex()))
            elif(randomInt == 2):
                character = RPGCharacter(Rogue(), int(self.levelBox.currentIndex()))
            elif(randomInt == 3):
                character = RPGCharacter(Ranger(), int(self.levelBox.currentIndex()))
            elif(randomInt == 4):
                character = RPGCharacter(Wizard(), int(self.levelBox.currentIndex()))
            else:
                character = RPGCharacter(Cleric(), int(self.levelBox.currentIndex()))
        elif (self.classBox.currentText() == "Random Warrior"):
            randomInt = random.randrange(1, 3)
            if(randomInt == 1):
                character = RPGCharacter(Fighter(), int(self.levelBox.currentIndex()))
            elif(randomInt == 2):
                character = RPGCharacter(Rogue(), int(self.levelBox.currentIndex()))
            elif(randomInt == 3):
                character = RPGCharacter(Ranger(), int(self.levelBox.currentIndex()))
        elif (self.classBox.currentText() == "Random Spellcaster"):
            randomInt = random.randrange(1, 2)
            if(randomInt == 1):
                character = RPGCharacter(Wizard(), int(self.levelBox.currentIndex()))
            else:
                character = RPGCharacter(Cleric(), int(self.levelBox.currentIndex()))
        elif (self.classBox.currentText() == "Fighter"):
            character = RPGCharacter(Fighter(), int(self.levelBox.currentIndex()))
        elif (self.classBox.currentText() == "Rogue"):
            character = RPGCharacter(Rogue(), int(self.levelBox.currentIndex()))
        elif (self.classBox.currentText() == "Ranger"):
            character = RPGCharacter(Ranger(), int(self.levelBox.currentIndex()))
        elif (self.classBox.currentText() == "Wizard"):
            character = RPGCharacter(Wizard(), int(self.levelBox.currentIndex()))
        else:
            character = RPGCharacter(Cleric(), int(self.levelBox.currentIndex()))

        character.generateStats(self.statGenBox.currentText())
        charStats = character.stats
        character.selectWeapon()
        character.genFeats()
        
        #print("Test")
        self.strBox.setText(str(charStats[1]))
        #self.statusBar().showMessage('Character Generated')
        
        
if __name__ == '__main__':
    import sys
 
    app = QtGui.QApplication(sys.argv)
 
    helloPythonWidget = BasicWidget()
    helloPythonWidget.show()
 
    sys.exit(app.exec_())
    
