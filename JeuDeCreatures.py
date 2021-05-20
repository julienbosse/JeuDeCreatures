from random import choice

class Case:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def adjacentes(self,jeu):
        # Retourne les cases de la liste des cases dont la distance**2 est inférieure ou égale à 2 à la case courante
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
        print("########## DÉBUT DU JEU ##########")

    def estOccupee(self,case):
        for creature in self.listeDesCreatures:
            if creature.position.x == case.x and creature.position.y == case.y:
                return True
        
        return False


    def deplacer(self,creature,case):
        print("_____ DEPLACEMENT ______")
        print("Tour :", self.tour)
        print("C'est à", self.actif, "de jouer")
        if self.actif == creature :
            listeAdjacentes = creature.position.adjacentes(self)

            for c in listeAdjacentes :
                if c.x == case.x and c.y == case.y:
                    print("La case est bien adjacente")

                    print("La case est occupée ?",self.estOccupee(case))
                    if self.estOccupee(case):
                        print("### Vainqueur :", creature.nom)
                        self.tour = 0
                    else:
                        creature.position.x = case.x
                        creature.position.y = case.y
                        self.actif = listeDesCreatures[self.tour%2]
                        self.tour += 1
                        print("\n")
                    break

            return None
        else :
            print("Ce n'est pas à vous de jouer")
            return None

    def plateau(self):
        i=0
        for x in range(int(len(self.listeDesCases)**(1/2))):
            print("|",end="")
            for y in range(int(len(self.listeDesCases)**(1/2))):
                if self.estOccupee(self.listeDesCases[i]):
                    print(" X |",end="")
                else:
                    print(" _ |",end="")
                i+=1
            print()
        print()

    def __str__(self):
        s = str(self.listeDesCases)+"\n"+str(self.listeDesCreatures)+"\n"+str(self.tour)+str(self.actif)
        return s

class Creature:

    def __init__(self,nom,position):
        self.nom=nom
        self.position=position

    def choisirCible(self,jeu):
        print("___ CHOIX DE LA CIBLE ___")
        listeAdjacentes = self.position.adjacentes(jeu)
        # for i in listeAdjacentes: print(i)
        for c in listeAdjacentes:
            if jeu.estOccupee(c) :
                print("Cible occupée ", c)
                print(c)
                return c

        cible = choice(listeAdjacentes)
        print("Cible aléatoire ", cible)
        return cible

    def __str__(self):
        return str(self.nom)+" | "+str(self.position)


crea1 = Creature("Dragon",Case(4,4))
crea2 = Creature("Phoenix",Case(0,0))
listeDesCreatures = [crea1, crea2]
listeDesCases = [Case(x,y) for x in range(4) for y in range(4)]

jeu = Jeu(listeDesCases, listeDesCreatures, 1, crea1)

i=0

compteur = 1

from time import sleep

while jeu.tour != 0:
    sleep(0.5)
    jeu.plateau()
    cible = listeDesCreatures[i%2].choisirCible(jeu)
    jeu.deplacer(listeDesCreatures[i%2],cible)
    i+=1