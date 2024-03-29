class Choix:
    
    def __init__(self, choix):

        self.choix = choix
        self.continu = []

    def calculerChoix(self, lab):
        if (lab[self.choix[0], self.choix[1]+1] != 'X'):
            self.continu.append(Choix((self.choix[0], self.choix[1]+1)))
        if (lab[self.choix[0]+1, self.choix[1]] != 'X'):
            self.continu.append(Choix((self.choix[0]+1, self.choix[1])))
        if (lab[self.choix[0], self.choix[1]-1] != 'X'):
            self.continu.append(Choix((self.choix[0], self.choix[1]-1)))
        if (lab[self.choix[0]-1, self.choix[1]] != 'X'):
            self.continu.append(Choix((self.choix[0]-1, self.choix[1])))

    def isCulDeSac(self, lab):
        mur = 0
        if (lab[self.choix[0], self.choix[1]+1] == 'X'):
            mur += 1
        if (lab[self.choix[0]+1, self.choix[1]] == 'X'):
            mur += 1
        if (lab[self.choix[0], self.choix[1]-1] == 'X'):
            mur += 1
        if (lab[self.choix[0]-1, self.choix[1]] == 'X'):
            mur += 1
        return mur >= 3
    
    def calculerContinu(self, lab):
        for choix in self.continu:
            choix.calculerChoix()
            if choix.isCulDeSac(lab):
                continue
            else:
                choix.calculerContinu(lab)
