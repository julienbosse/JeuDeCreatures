from random import choice

class Case:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def adjacentes(self,jeu):
        # Retourne les cases de la liste des cases dont la distance est inférieure à 2 à la case courante
        return [c for c in jeu.listeDesCases if 0 < (c.x-self.x)**2+(c.y-self.y)**2 <= 2]
        

    def __str__(self):
        s = "(x: "+str(self.x)+", y: "+str(self.y)+")"
        return s
        


class Jeu:
    def __init__(self,listeDesCases,listeDesCreatures,tour,actif):
        self.listeDesCases=listeDesCases
        self.listeDesCreatures=listeDesCreatures
        self.tour=tour
        self.actif=actif

    def estOccupee(self,case):
        for creature in self.listeDesCreatures:
            if creature.position.x == case.x and creature.position.y == case.y:
                return True
        
        return False


    def deplacer(self,creature,case):
        if self.actif == creature : 
            print("C'est bien à vous de jouer")
            listeAdjacentes = case.adjacentes(self)
            for i in listeAdjacentes: print(i)
            if case in listeAdjacentes:
                print("La case est bien adjacente")
                creature.x = case.x
                creature.y = case.y
                if self.estOccupee(case):
                    print("Vainqueur : ", creature.nom)
                else: 
                    self.tour += 1
                    self.actif = listeDesCreatures[listeDesCreatures.index(creature)+1]
                    print("Tour :", self.tour)
                    print("Actif :", self.actif)
            return None
        else :
            print("Ce n'est pas à vous de jouer")
            return None

    def __str__(self):
        s = str(self.listeDesCases)+"\n"+str(self.listeDesCreatures)+"\n"+str(self.tour)+str(self.actif)
        return s

class Creature:

    def __init__(self,nom,position):
        self.nom=nom
        self.position=position

    def choisirCible(self,jeu):
        listeAdjacentes = self.position.adjacentes(jeu)
        # for i in listeAdjacentes: print(i)
        for c in listeAdjacentes:
            if jeu.estOccupee(c) :
                print("Target acquired")
                print(c)
                return c
        return choice(listeAdjacentes)

    def __str__(self):
        return str(self.nom)+" | "+str(self.position)

print("______ LANCEMENT ______")

crea1 = Creature("Dragon",Case(0,0))
crea2 = Creature("Phoenix",Case(1,1))
listeDesCreatures = [crea1, crea2]
listeDesCases = [Case(x,y) for x in range(4) for y in range(4)]

jeu = Jeu(listeDesCases, listeDesCreatures, 1, crea1)

cc = crea1.choisirCible(jeu)

jeu.deplacer(crea1,Case(1,1))
print(crea1.position)