class Arbre:

    def __init__(self, racine=None, g=None, d=None):
        self.racine = racine
        self.g = g
        self.d = d


def inserer(A, val, pos):
    if pos == 'r':
        A.racine = val

    elif pos == 'g':
        A.g = Arbre(val)

    else:
        A.d = Arbre(val)


def preorder(A):
    if A != None:
        print(A.racine)
        preorder(A.g)
        preorder(A.d)


def inorder(A):
    if A != None:
        preorder(A.g)
        print(A.racine)
        preorder(A.d)


def postorder(A):
    if A != None:
        preorder(A.g)
        preorder(A.d)
        print(A.racine)


def niveau(A, n):
    if A != None:
        if n == 0:
            print(A.racine)
        else:
            niveau(A, n - 1)
            niveau(A, n - 1)


def nombreNoeudNiveau(A, n):
    if A != None:
        if n == 0:
            return 1
        else:
            return nombreNoeudNiveau(A, n - 1) + nombreNoeudNiveau(A, n - 1)

    else:
        return 0


def nombreDeNiveaux(A):
    i = 0
    while nombreNoeudNiveau(A, i):
        i += 1
    return i


def nombreDeNiveauxRec(A):
    if A != None:
        return 1 + max(nombreDeNiveauxRec(A.g), nombreDeNiveauxRec(A.d))
    else:
        return 0


def affichageEnLargeur(A):
    n = nombreDeNiveauxRec(A)
    for i in range(n):
        niveau(A, i)
        