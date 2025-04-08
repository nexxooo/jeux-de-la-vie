from random import * 
class Game:
    def __init__(self,h,l,t):
        self.hauteur = h
        self.largeur = l
        self.tab = t 
    
    def dead_state(self):
        res = [[0] * self.largeur for _ in range(self.hauteur)]
        self.tab = res

    
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
    
    def avancer(self):
        direction = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
        res = [[0] * self.largeur for _ in range(self.hauteur)]
        for ligne in range(len(self.tab)):
            for colone in range(len(self.tab[ligne])):
                nombre_voisin = 0
                for dx, dy in direction:
                    ni = ligne + dx
                    nj = colone + dy
                    if 0 <= ni < self.hauteur and 0 <= nj < self.largeur:
                        nombre_voisin += self.tab[ni][nj]

                if self.tab[ligne][colone] == 1:
                    if nombre_voisin in [0,1]:
                        res[ligne][colone]= 0
                    elif nombre_voisin in [2,3]:
                        res[ligne][colone]=1
                    elif nombre_voisin > 3:
                        res[ligne][colone] = 0
                else:
                    if nombre_voisin ==3:
                        res[ligne][colone] = 1
        self.tab = res


                     




#print(dead_state(2,2))
test = Game(3,3,[
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ])
print(test)
test.avancer()
print("__________________")
print(test)

