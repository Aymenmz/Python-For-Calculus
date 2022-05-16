class Arbre:

    def __init__(self, data=None, filsG=None, filsD=None):
        self.data = data
        self.filsD = filsD
        self.filsG = filsG


def insert(A, data, position):
    if position == 'r':
        A.data = data

    elif position == 'g':
        A.filsG = Arbre(data)

    else:
        A.filsD = Arbre(data)


A = Arbre()
insert(A, 'B', 'g')
insert(A, 'C', 'd')
insert(A.filsG, 'D', 'g')
insert(A.filsG, 'E', 'd')
insert(A.filsD, 'F', 'g')
insert(A.filsD, 'G', 'd')


def pre_order(A):
    if A is not None:
        print(A.data)
        pre_order(A.filsG)
        pre_order(A.filsD)


def in_order(A):
    if A is not None:
        in_order(A.filsG)
        print(A.data)
        in_order(A.filsD)


def post_order(A):
    if A is not None:
        post_order(A.filsG)
        post_order(A.filsD)
        print(A.data)


# qui permet d’afficher le niveau N
def niveau(A, n):
    if A != None:
        if n == 0:
            print(A.data)
        else:
            niveau(A.g, n - 1)
            niveau(A.d, n - 1)


# qui retourne le nombre de Noeuds d’un niveau N
def nombreDeNoeudsParNiveau (A,n):
    if A!= None:
        if n == 0:
            return 1
        else:
            return nombreDeNoeudsParNiveau(A.filsG, n-1) + nombreDeNoeudsParNiveau(A.filsD)
    else:
        return 0

# qui retourne le nombre de niveaux
def nombreDeNiveaux (A):
    cpt = 0
    while nombreDeNoeudsParNiveau(A, cpt)!= 0:
        cpt += 1
    return cpt

# qui retourne le nombre de Noeuds dans un arbre
def nombreDeNoeuds (A):
    cpt = 0
    for i in range(nombreDeNiveaux(A)):
        cpt += nombreDeNoeudsParNiveau(A, i)
    return cpt




















