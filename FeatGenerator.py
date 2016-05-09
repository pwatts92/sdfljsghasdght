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
        self.feats.append(Feat("Weapon Focus", 1, 1, 1, 0).requirement(1, 0, 0 , 0 , 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Spell Focus", 0, 0, 0, 1).requirement(0, 1, 0 , 0 , 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Dodge", 0, 1, 0.5, 0).requirement(0, 0, 0 , 13, 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Point-Blank Shot", 0, 0, 1, 0).requirement(0, 0, 0 , 13, 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Precise Shot", 0, 0, 1, 0).requirement(0, 0, 0 , 13, 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Toughness", 1, 1, 0, 0).requirement(0, 0, 0 , 13, 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Improved Initiative", 0.5, 1, 1, 1).requirement(0, 0, 0 , 0 , 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Improved Trip", 1, 1, 0, 0).requirement(1, 0, 0 , 0 , 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Improved Disarm", 1, 1, 0, 0).requirement(1, 0, 0 , 0 , 0 , 0 , 0 , 0, []))
        self.feats.append(Feat("Improved Feint", 0.5, 1, 0, 0).requirement(1, 0, 0 , 0 , 0 , 0 , 0 , 0, []))

        
    def featSet(self, priority):
        Heavy = 1
        Light = 2
        Ranged = 3
        '''
        if(priority == Heavy):
            self.feats.sort(key=lambda feat: feat.heavPriority)
        elif(priority == Light):
            self.feats.sort(key=lambda Feat: Feat.lightPriority)
        elif(priority == Ranged):
            self.feats.sort(key=lambda Feat: Feat.rangePriority)
        else:
            self.feats.sort(key=lambda Feat: Feat.magePriority)
            '''
        return sorted(self.feats)
    
    
    
class Feat(object):
    def __init__(self, name, heavPriority, lightPriority, rangePriority, magePriority):
        self.name = name
        self.heavPriority = heavPriority
        self.lightPriority = lightPriority
        self.rangePriority = rangePriority 
        self.magePriority = magePriority
        
    def __repr__(self, *args, **kwargs):
        return repr((self.heavPriority, self.lightPriority, self.rangePriority, self.magePriority))
        
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