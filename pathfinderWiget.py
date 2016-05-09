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
        
        self.nameCLabel = QtGui.QLabel("Class", self)
        self.nameCLabel.move(220, 100)
        self.nameCBox = QtGui.QTextEdit(self)
        self.nameCBox.move(200, 130)
        
        self.attackLabel = QtGui.QLabel("Attack Bonus", self)
        self.attackLabel.move(200, 170)
        self.attackBox = QtGui.QTextEdit(self)
        self.attackBox.move(200, 200)
        
        self.refLabel = QtGui.QLabel("Reflex Save", self)
        self.refLabel.move(350, 100)
        self.refBox = QtGui.QTextEdit(self)
        self.refBox.move(350, 130)
        
        self.fortLabel = QtGui.QLabel("Fortitude Save", self)
        self.fortLabel.move(350, 170)
        self.fortBox = QtGui.QTextEdit(self)
        self.fortBox.move(350, 200)
        
        self.willLabel = QtGui.QLabel("Will Save", self)
        self.willLabel.move(350, 230)
        self.willBox = QtGui.QTextEdit(self)
        self.willBox.move(350, 260)
        
        self.weaponLabel = QtGui.QLabel("Weapon", self)
        self.weaponLabel.move(250, 300)
        self.weaponBox = QtGui.QTextEdit(self)
        self.weaponBox.resize(300, 40)
        self.weaponBox.move(250, 330)
        
        self.featLabel = QtGui.QLabel("Feats", self)
        self.featLabel.move(600, 100)
        self.featBox = QtGui.QTextEdit(self)
        self.featBox.resize(300, 250)
        self.featBox.move(600, 130)
        
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
        self.setWindowTitle("RPG Character Generator")
        
    def generateCharacter(self):
        #classText = self.classBox.currentText()
        if (self.classBox.currentText() == "Random"):
            randomInt = random.randrange(1, 5)
            if(randomInt == 1):
                character = RPGCharacter(Fighter(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Fighter")
            elif(randomInt == 2):
                character = RPGCharacter(Rogue(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Rogue")
            elif(randomInt == 3):
                character = RPGCharacter(Ranger(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Ranger")
            elif(randomInt == 4):
                character = RPGCharacter(Wizard(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Wizard")
            else:
                character = RPGCharacter(Cleric(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Cleric")
        elif (self.classBox.currentText() == "Random Warrior"):
            randomInt = random.randrange(1, 3)
            if(randomInt == 1):
                character = RPGCharacter(Fighter(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Fighter")
            elif(randomInt == 2):
                character = RPGCharacter(Rogue(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Rogue")
            elif(randomInt == 3):
                character = RPGCharacter(Ranger(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Ranger")
        elif (self.classBox.currentText() == "Random Spellcaster"):
            randomInt = random.randrange(1, 2)
            if(randomInt == 1):
                character = RPGCharacter(Wizard(), int(self.levelBox.currentIndex()))
                self.nameCBox.setText("Wizard")
            else:
                character = RPGCharacter(Cleric(), int(self.levelBox.currentIndex()))
        elif (self.classBox.currentText() == "Fighter"):
            character = RPGCharacter(Fighter(), int(self.levelBox.currentIndex()))
            self.nameCBox.setText("Fighter")
        elif (self.classBox.currentText() == "Rogue"):
            character = RPGCharacter(Rogue(), int(self.levelBox.currentIndex()))
            self.nameCBox.setText("Rogue")
        elif (self.classBox.currentText() == "Ranger"):
            character = RPGCharacter(Ranger(), int(self.levelBox.currentIndex()))
            self.nameCBox.setText("Ranger")
        elif (self.classBox.currentText() == "Wizard"):
            character = RPGCharacter(Wizard(), int(self.levelBox.currentIndex()))
            self.nameCBox.setText("Wizard")
        else:
            character = RPGCharacter(Cleric(), int(self.levelBox.currentIndex()))
            self.nameCBox.setText("Cleric")

        character.generateStats(self.statGenBox.currentText())
        charStats = character.stats
        character.selectWeapon()
        featSet = character.genFeats()
    
        self.strBox.setText(str(charStats[0]))
        self.dexBox.setText(str(charStats[1]))
        self.conBox.setText(str(charStats[2]))
        self.intBox.setText(str(charStats[3]))
        self.wisBox.setText(str(charStats[4]))
        self.chaBox.setText(str(charStats[5]))
        
        self.attackBox.setText(str(character.RPGClass.attackBonus(character.level) + ((charStats[0]-10)/2) + ((charStats[1]-10)/2) ))
        if(character.RPGClass.saveArray[0] == 0):
            self.refBox.setText(str((charStats[1]-10)/2 + self.levelBox.currentIndex() / 2))
        else:
            self.refBox.setText(str((charStats[1]-10)/2 + self.levelBox.currentIndex() + 2))
        if(character.RPGClass.saveArray[1] == 0):
            self.fortBox.setText(str((charStats[2]-10)/2 + self.levelBox.currentIndex() / 2))
        else:
            self.fortBox.setText(str((charStats[2]-10)/2 + self.levelBox.currentIndex() + 2))
        if(character.RPGClass.saveArray[2] == 0):
            self.willBox.setText(str((charStats[4]-10)/2 + self.levelBox.currentIndex() / 2))
        else:
            self.willBox.setText(str((charStats[4]-10)/2 + self.levelBox.currentIndex() + 2))   
        
        #weaponStr = character.weapon.weaponName + ", " + character.weapon.weaponDamage + "+" + str(((charStats[0]-10)/2) + ((charStats[1]-10)/2)) + ", " + character.weapon.weaponCrit)
        weaponStr = character.weapon.weaponName + ", " + character.weapon.weaponDamage + "+" + str((charStats[0]-10)/2 + ((charStats[1]-10)/2)) + ", " + character.weapon.weaponCrit
        self.weaponBox.setText(weaponStr)
        
        #for i < len(featSet):
            
        
if __name__ == '__main__':
    import sys
 
    app = QtGui.QApplication(sys.argv)
 
    helloPythonWidget = BasicWidget()
    helloPythonWidget.show()
 
    sys.exit(app.exec_())
    
