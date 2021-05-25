from random import choice

class Case:

    def __init__(self,x: int,y: int):
        self.x = x
        self.y = y

    def adjacentes(self,jeu) -> list:
        # Retourne les cases de la liste des cases dont la distance**2 est inférieure ou égale à 2 à la case courante
        return [c for c in jeu.listeDesCases if 0 < (c.x-self.x)**2+(c.y-self.y)**2 <= 2]
        

    def __str__(self):
        s = "(x: "+str(self.x)+", y: "+str(self.y)+")"
        return s
        
class Creature:

    def __init__(self, nom: str, position: Case):
        self.nom=nom
        self.position=position

    def choisirCible(self, jeu):
        print("___ CHOIX DE LA CIBLE ___")
        listeAdjacentes = self.position.adjacentes(jeu)
        for c in listeAdjacentes:
            if jeu.estOccupee(c) :
                # print("Cible occupée ", c)
                return c

        cible = choice(listeAdjacentes)
        # print("Cible aléatoire ", cible)
        return cible

    def __str__(self):
        return str(self.nom)+" | "+str(self.position)

class Jeu:
    def __init__(self,listeDesCases: list,listeDesCreatures: list):
        self.listeDesCases=listeDesCases
        self.listeDesCreatures=listeDesCreatures
        self.tour=1
        self.actif=listeDesCreatures[0]
        
        print("########## DÉBUT DU JEU ##########")

    def estOccupee(self,case):
        for creature in self.listeDesCreatures:
            if creature.position.x == case.x and creature.position.y == case.y:
                return True
        
        return False


    def deplacer(self,creature,case):
        print("______ DEPLACEMENT ______")
        print("Tour :", self.tour)
        print("C'est à", self.actif, "de jouer")
        if self.actif == creature :
            listeAdjacentes = creature.position.adjacentes(self)

            for c in listeAdjacentes :
                if c.x == case.x and c.y == case.y:
                    if self.estOccupee(case):
                        creature.position.x = case.x
                        creature.position.y = case.y
                        print()
                        print("################################")
                        print("  ### Vainqueur :  "+ creature.nom + "  ###")
                        print("################################")
                        self.tour = 0
                    else:
                        creature.position.x = case.x
                        creature.position.y = case.y
                        self.actif = listeDesCreatures[self.tour%len(listeDesCreatures)]
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
                    for c in listeDesCreatures:
                        if c.position.x == listeDesCases[i].x and c.position.y == listeDesCases[i].y:
                            print(" "+c.nom[0]+" |",end="")
                else:
                    print(" _ |",end="")
                i+=1
            print()
        print()

    def __str__(self):
        s = str(self.listeDesCases)+"\n"+str(self.listeDesCreatures)+"\n"+str(self.tour)+str(self.actif)
        return s

from time import sleep

# Création de la partie
xmax=8
ymax=8

crea1 = Creature("Garurumon",Case(xmax,ymax))
crea2 = Creature("Dreymon",Case(0,0))
crea3 = Creature("MetalGreymon", Case(0,ymax))
listeDesCreatures = [crea1, crea2, crea3]

listeDesCases = [Case(x,y) for x in range(xmax) for y in range(ymax)]

jeu = Jeu(listeDesCases, listeDesCreatures)

# Boucle partie : affiche le plateau, choisit la cible pour la créature active et déplace cette dernière jusqu'à ce qu'il y ait un vainqueur
i=0
while jeu.tour != 0:
    sleep(0.5)
    jeu.plateau()
    cible = listeDesCreatures[i%len(listeDesCreatures)].choisirCible(jeu)
    jeu.deplacer(listeDesCreatures[i%len(listeDesCreatures)],cible)
    i+=1
