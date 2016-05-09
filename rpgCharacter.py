'''
Created on Apr 28, 2016

@author: parker
'''
from Main.rpgClass import RPGClass
import random

class RPGCharacter(object):
    '''
    classdocs
    '''
    
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

    def __init__(self, RPGClass, level):
        '''
        Constructor
        '''
        self.level = level
        self.RPGClass = RPGClass
        self.stats = []
        
    def generateStats(self, statType):
        statList = []
        while len(statList) < 6:
            if statType == "Minion":
                stat = random.randrange(2, 6) + random.randrange(2, 6) + random.randrange(2, 6)
            elif statType == "Normal":
                statArray = []
                statArray.append(random.randrange(2, 6))
                statArray.append(random.randrange(2, 6))
                statArray.append(random.randrange(2, 6))
                statArray.append(random.randrange(2, 6))
                statArray.sort(cmp=None, key=None, reverse=False)
                #statArray = sorted(random.randrange(1, 6), random.randrange(1, 6), random.randrange(1, 6), random.randrange(1, 6))
                stat = statArray.pop() + statArray.pop() + statArray.pop()
            elif statType == "Mighty":
                statArray = sorted([random.randrange(2, 6), random.randrange(2, 6), random.randrange(2, 6)])
                stat = statArray.pop() + statArray.pop() + 6
            statList.append(stat)
        statList.sort()
        
        priorities = self.RPGClass.statPriority()
        
        while len(statList) > 0:
            self.stats.insert(priorities.pop(), statList.pop())
            
    def selectWeapon(self):
        self.weapon = Weapon(self.RPGClass.weaponProficiency, self.RPGClass.fightingStyle)
        
    def genFeats(self):
        featArray = self.RPGClass.featProgression(self.level)
        x = 0
        y = len(featArray)
        self.featSequence = []

        while x < len(featArray):
            self.featSequence.append(featArray[x])
        return self.featSequence
            
class Weapon(object):
    
    Martial = 1
    Simple = 2
    Rogue = 3
    
    Heavy = 1
    Light = 2
    Ranged = 3
    
    def __init__(self, weaponProficiency, fightingStyle):
        self.weaponGen(weaponProficiency, fightingStyle)
        self.weaponType = weaponProficiency
        self.weaponWeight = fightingStyle
        self.weaponStringDesc = iter(self.weaponSet.pop(self.weaponIndex))
        self.weaponName = self.weaponStringDesc.next()
        self.weaponDamage = self.weaponStringDesc.next()
        self.weaponCrit = self.weaponStringDesc.next()
        
    def weaponGen(self, weaponProficiency, fightingStyle):
        self.weaponSet = []
        if(weaponProficiency == self.Martial):
            if(fightingStyle == self.Heavy):
                self.weaponSet.append(["Greatsword", "2d6", "19-20/x2"])
                self.weaponSet.append(["Earthbreaker", "2d6", "20/x3"])
                self.weaponSet.append(["Longsword", "1d8", "19-20/x2"])
                self.weaponSet.append(["Warhammer", "1d8", "20/x3"])
                self.weaponSet.append(["Greataxe", "1d12", "20/x3"])
                self.weaponSet.append(["Halberd", "1d10", "20/x3"])
                self.weaponSet.append(["Scythe", "2d4", "20/x4"])
                self.weaponSet.append(["Heavy Flail", "1d10", "19-20/x2"])
            elif(fightingStyle == self.Light):
                self.weaponSet.append(["Rapier", "1d6", "18-20/x2"])
                self.weaponSet.append(["Scimitar", "1d6", "18-20/x2"])
                self.weaponSet.append(["Light Hammer", "1d4", "20/x2"])
                self.weaponSet.append(["Handaxe", "1d6", "20/x3"])
                self.weaponSet.append(["Kukri", "1d4", "18-20/x2"])
            else:
                self.weaponSet.append(["Longbow", "1d8", "20/x3"])
                self.weaponSet.append(["Shortbow", "1d6", "20/x3"])
        elif(weaponProficiency == self.Rogue):
            if(fightingStyle == self.Heavy):
                self.weaponSet.append(["Spear", "1d8", "20/x3"])
                self.weaponSet.append(["Heavy Mace", "1d8", "20/x2"])
                self.weaponSet.append(["Morningstar", "1d8", "20/x2"])
            elif(fightingStyle == self.Light):
                self.weaponSet.append(["Rapier", "1d6", "18-20/x2"])
                self.weaponSet.append(["Shortsword", "1d6", "18-20/x2"])
                self.weaponSet.append(["Sap", "1d4", "18-20/x2"])
                self.weaponSet.append(["Dagger", "1d4", "19-20/x2"])
            else:
                self.weaponSet.append(["Shortbow", "1d6", "20/x3"])
                self.weaponSet.append(["Crossbow", "1d8", "19-20/x3"])
        else:
            if(fightingStyle == self.Heavy):
                self.weaponSet.append(["Spear", "1d8", "20/x3"])
                self.weaponSet.append(["Heavy Mace", "1d8", "20/x2"])
                self.weaponSet.append(["Morningstar", "1d8", "20/x2"])
            elif(fightingStyle == self.Light):
                self.weaponSet.append(["Dagger", "1d4", "19-20/x2"])
                self.weaponSet.append(["Light Mace", "1d6", "20/x2"])
                self.weaponSet.append(["Sickle", "1d6", "20/x2"])
            else:
                self.weaponSet.append(["Crossbow", "1d8", "19-20/x3"])
        
        self.weaponIndex = random.randrange(0, len(self.weaponSet))
