'''
Created on Apr 28, 2016

@author: parker
'''

import random
from duplicity.log import LevelName

class RPGClass():

    STR = 1 
    DEX = 2 
    CON = 3
    INT = 4
    WIS = 5
    CHA = 6

    Martial = 1
    Simple = 2
    Rogue = 3
    
    Heavy = 1
    Light = 2
    Ranged = 3

    def __init__(self):
        self.saveArray = []
        self.statPriorities = []
        self.weaponProficiency = 0
        self.fightingStyle = 0
        self.spellSet = []
        for x in range(0, 9):
            self.spellSet.append([])
        
    def attackBonus(self, level):
        self.level = level
        return self.bab * level
    
    def saves(self):
        return self.saveArray

    def statPriority(self):
        return self.statPriorities
    
    def featProgression(self):
        self.featArray = []
        for x in range (0, self.level):
            if x%2 == 1:
                self.featArray.append(x)
        

class Fighter(RPGClass):
    
    bab = 1
    
    def __init__(self):
        RPGClass.__init__(self)
        self.saveArray.append(1)
        self.saveArray.append(0)
        self.saveArray.append(0)
        
        if random.randrange(1, 3) == 1:
            self.statPriorities.append(self.DEX)
            self.statPriorities.append(self.CON)
            self.statPriorities.append(self.STR)
            if random.randrange(1, 2) == 1:
                self.fightingStyle = self.Ranged
            else:
                self.fightingStyle = self.Light
        else:
            self.statPriorities.append(self.STR)
            self.statPriorities.append(self.CON)
            self.statPriorities.append(self.DEX)
            self.fightingStyle = self.Heavy
        self.statPriorities.append(self.INT)
        self.statPriorities.append(self.WIS)
        self.statPriorities.append(self.CHA)

        self.weaponProficiency = self.Martial
        
    def featProgression(self):
        self.featArray = []
        self.featArray.append(1)
        for x in range (1, self.level):
            self.featArray.append(x)
            
            
class Rogue(RPGClass):
    
    bab = 0.75
    
    def __init__(self):
        RPGClass.__init__(self)
        self.saveArray.append(0)
        self.saveArray.append(1)
        self.saveArray.append(0)
        
        if random.randrange(1, 5) != 1:
            self.statPriorities.append(self.DEX)
            self.statPriorities.append(self.CON)
            self.statPriorities.append(self.INT)
            self.statPriorities.append(self.WIS)
            self.statPriorities.append(self.CHA)
            self.statPriorities.append(self.STR)
            if random.randrange(1, 4) == 1:
                self.fightingStyle = self.Ranged
            else:
                self.fightingStyle = self.Light
        else:
            self.statPriorities.append(self.STR)
            self.statPriorities.append(self.CON)
            self.statPriorities.append(self.DEX)
            self.statPriorities.append(self.INT)
            self.statPriorities.append(self.WIS)
            self.statPriorities.append(self.CHA)
            self.fightingStyle = self.Heavy
        self.weaponProficiency = self.Rogue
        
class Ranger(RPGClass):
    
    bab = 1
    
    def __init__(self):
        RPGClass.__init__(self)
        self.saveArray.append(1)
        self.saveArray.append(1)
        self.saveArray.append(0)
        
        if random.randrange(1, 3) != 1:
            self.statPriorities.append(self.DEX)
            self.statPriorities.append(self.CON)
            self.statPriorities.append(self.STR)
            if random.randrange(1, 2) == 1:
                self.fightingStyle = self.Ranged
            else:
                self.fightingStyle = self.Light
        else:
            self.statPriorities.append(self.STR)
            self.statPriorities.append(self.CON)
            self.statPriorities.append(self.DEX)
            self.fightingStyle = self.Heavy
        self.statPriorities.append(self.WIS)
        self.statPriorities.append(self.CHA)
        self.statPriorities.append(self.INT)

        self.weaponProficiency = self.Martial
        
    def featProgression(self):
        self.featArray = []
        for x in range (0, self.level):
            if x%2 == 1 or (x-2)%4 == 0:
                self.featArray.append(x)
                