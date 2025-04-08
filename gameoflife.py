from random import * 
class Game:
    def __init__(self,h,l):
        self.hauteur = h
        self.largeur = l
        self.tab = self.random_state()
    
    def dead_state(self):
        res = [[0] * self.largeur for _ in range(self.hauteur)]
        return res
    def random_state(self):
        tab = self.dead_state()
        for i in tab:
            for y in range(len(i)):
                i[y] = randint(0,1)
        return tab

    def __str__(self):
        res =""
        for ligne in self.tab:
            ch = ""
            for cellule in ligne:
                if cellule== 0:
                    ch+= "☐ "
                else:
                    ch+= "■ "    
            res += ch + "\n"    
        return res     


#print(dead_state(2,2))
test = Game(5,5)
print(test)