class Case:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def adjacentes(self,Jeu):
        return None

    def __repr__(self):
        return repr((self.x,self.y))


class Jeu:
    def __init__(self,listeDesCases,listeDesCreatures,tour,actif):
        self.listeDesCases=listeDesCases
        self.listeDesCreatures=listeDesCreatures
        self.tour=tour
        self.actif=actif

    def estOccuper(self,Case):
        return None

    def deplacer(self,Creature,Case):
        return None

class Creature:

    def __init__(self,nom,position):
        self.nom=nom
        self.position=position

    def choisirCible(jeu):
        return None

c = Case(0,1)
print(c)