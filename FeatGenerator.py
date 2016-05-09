'''
Created on May 8, 2016

@author: parker
'''

class FeatSelector(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.feats = []
        
        #Needs to be filled
        self.feat.append(Feat("Weapon Focus", 1, 1, 1, 0).requirement(1, 0, 0 , 0 , 0 , 0 , 0 , 0, []))
        self.feat.append(Feat("Spell Focus", 0, 0, 0, 1).requirement(0, 1, 0 , 0 , 0 , 0 , 0 , 0, []))
        self.feat.append(Feat("Dodge", 0, 1, 0.5, 0).requirement(0, 0, 0 , 13, 0 , 0 , 0 , 0, []))
        
    def featSet(self, priority):
        Heavy = 1
        Light = 2
        Ranged = 3
        
        if(priority == Heavy):
            self.feats.sort(cmp=self.heavPriority, key=None, reverse=False)
        elif(priority == Light):
            self.feats.sort(cmp=self.lightPriority, key=None, reverse=False)
        elif(priority == Ranged):
            self.feats.sort(cmp=self.rangedPriority, key=None, reverse=False)
        else:
            self.feats.sort(cmp=self.magePriority, key=None, reverse=False)
            
        return self.feats
    
    
    
class Feat(object):
    def __init__(self, name, heavPriority, lightPriority, rangePriority, magePriority):
        self.name = name
        self.heavPriority = heavPriority
        self.lightPriority = lightPriority
        self.rangePriority = rangePriority 
        self.magePriority = magePriority
        
    def requirement(self, BAB, CL, STR, DEX, CON, INT, WIS, CHA, feats):
        self.BAB = BAB
        self.CL = CL
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.feats = feats