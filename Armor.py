import Game


class Armor:
    # level,classtype,name,type,basedef,durability
    def __init__(self, armorlevel, armorclasstype, armorname, armortype, armorbasedef, armordur):
        # level
        self.level = armorlevel

        # hero Class
        self.classtype = armorclasstype

        # hero Class
        self.type = armortype
        self.name = armorname

        # defense values
        self.basedefn = armorbasedef
        self.defn = self.basedefn

        # durability values
        self.maxdur = armordur
        self.dur = self.maxdur

    # damage durability, and check to see if broken
    def damagedur(self, aug, curve):
        self.dur -= int(aug * curve * .1)
        self.isbroken()
        pass

    # restore dur and check to see if fixed
    def restoredur(self, aug):
        self.dur += aug
        if self.dur > self.maxdur:
            self.dur = self.maxdur
        if not self.isbroken():
            self.defn = self.basedefn

    # repair entirely
    def repair(self):
        self.defn = self.basedefn
        self.dur = self.maxdur

    # 15% durability = stat reduction
    def isbroken(self):
        if self.dur <= 0:
            self.gearbreak()
            return True
        elif self.dur > 0:
            return False

    # this breaks the gear
    def gearbreak(self):
        self.atk = int(self.basedefn * .3)

    # prints all armor info
    def printarmorinfo(self):
        Game.marqueeprint('ARMOR')
        print(Game.lr_justify('Level:', str(self.level), 60))
        print(Game.lr_justify('Name:', str(self.name), 60))
        print(Game.lr_justify('Type:', str(self.type), 60))
        print(Game.lr_justify('Defense:', str(self.defn) + '/' + str(self.basedefn), 60))
        print(Game.lr_justify('Dur:', str(self.dur) + '/' + str(self.maxdur), 60))
        print(Game.lr_justify('Broken?:', str(self.isbroken()), 60))

    # ['Level', 'Name', 'Type', 'Defense', 'Dur', 'Broken?', 'Power']
    def datadict(self):
        return {'Level': str(self.level),
                'Name': str(self.name) + ' ' + str(self.type),
                'Def': str(self.defn),
                'Dur': str(self.dur) + '/' + str(self.maxdur),
                'Broken?': str(self.isbroken()),
                'Repair Cost': str(self.maxdur - self.dur) + ' gold'
                }
