"""
    facture =[1, ''Karim Naciri'',354.00,2019]
    dont facture[0] est le numéro de la facture, facture[1] le nom du client, 
    facture[2] le prix hors taxes (prixHT) de la facture 
    facture[3] l’année limite de paiement.
"""

# Q1. Définir la fonction lire() permettant de créer et de retourner une facture (liste) dont le numéro, nom, prix HT et
# année limite sont lus au clavier

from matplotlib.cbook import pts_to_midstep


def lire():
    num = int(input("entrer votre le numero de la facture : "))
    nom = input("entrer le nom : ")
    prix = float(input("entrer le prix : "))
    annee = input("entrer l'annee : ")

    return [num, nom, prix, annee]


# Q2. En utilisant la fonction lire(), définir la fonction lire_tous(n) permettant de lire les n factures non payées, dont
#   leurs informations sont lues au clavier, de les stocker dans une liste et de la retourner.

def lire_tous(n):
    all_factures = []
    for i in range(n):
        fact = lire()
        all_factures.append(fact)
    return all_factures


# Q3. Définir la fonction trier(factures) permettant de trier la liste des factures par ordre croissant des noms des
#   clients. Attention on ne pourra pas utiliser la méthode sort ni la fonction sorted.

def trier(factures):
    n = len(factures)

    for i in range(n - 1):
        if factures[i][1] > factures[i + 1][1]:
            factures[i][1], factures[i + 1][1] = factures[i + 1][1], factures[i][1]

    return factures


# Q4. En supposant que la liste des factures est triée par ordre croissant des noms des clients, et en utilisant une
# recherche dichotomique, définir la fonction recherche_dichotomique (factures, nom_client) retournant la facture
# correspondant au client dont le nom est passé en argument et liste vide sinon.

def recherche_dichotomique(factures, nom_client):
    mylist = []
    a = 0
    b = len(factures)

    while a <= b:
        m = (a + b) // 2
        if factures[m][1] == nom_client:
            return factures[m]

        elif factures[m][1] < nom_client:
            a = m + 1

        else:
            b = m - 1
    return []


# Q5. Ecrire une fonction d’entête maj_factures(factures) qui permet d’augmenter de 10% par an de retard les prix
# HT de toutes les factures dont l’année limite de paiement est strictement inférieure à l’année en cours (2021)
# Exemple : Soit la facture ayant l’année limite de paiement 2019 et le prixHT=100DH, le nouveau prix deviendra
# 121 DH. (De 2019 à 2020 on augmente le prix de 10% soit 110, de 2020 à 2021, on augmente 110 DH de
# 10% soit 121 DH)
def maj_factures(factures):
    n = len(factures)

    for i in range(n):
        if factures[i][3] < '2022':
            nbr_annees = 2022 - int(factures[i][3])
            for j in range(nbr_annees):
                factures[i][2] += factures[i][2] * 0.1
    return factures


# Ecrire la fonction total_TTC(factures) qui retourne la somme des prix totaux TTC (Toute Taxes Comprise)
# de toutes les factures dans la liste factures. La TVA étant fixée à 20% (0.2) (Prix TTC = PrixHT+ PrixHT* TVA)
def total_TTC(factures):
    prixTTC = 0
    n = len(factures)
    for i in range(n):
        prixTTC += factures[i][2] + factures[i][2] * 0.2
    return prixTTC


# Q7. Ecrire la fonction sauvgarderDansUnFichier(factures, nom_fichier) permettant de sauvegarder toutes les
# factures dans le fichier texte dont le nom est passé en argument.
def sauvgarderDansUnFichier(factures, nom_fichier):
    file = open("nom_fichier", "w")
    for i in range(len(factures)):
        file.write(str(factures[i][0]))
        file.write(',')
        file.write(factures[i][1])
        file.write(',')
        file.write(str(factures[i][2]))
        file.write(',')
        file.write(factures[i][3] + "\n")
    file.close()


# Q8. Ecrire la fonction sauvgarderDansUneBD(factures, nom_BD) permettant de sauvegarder toutes les factures
# dans la base de données dont le nom est passé en argument.
import sqlite3


def creeTable(nom_BD):
    db = sqlite3.connect(nom_BD)
    curs = db.cursor()
    curs.execute(''' CREATE TABLE FACTURE(
                         num integer primary key ,
                         nom varchar(30),
                         prix double ,
                         annee varchar(20)
        )''')
    db.commit()
    db.close()


def sauvgarderDansUneBD(factures, nom_BD):
    db = sqlite3.connect(nom_BD)
    curs = db.cursor()
    creeTable(nom_BD)
    insert_stat = '''insert into FACTURE(nom, prix, annee) values (?, ?, ?)'''
    for i in range(len(factures)):
        data = (factures[i][1], factures[i][2], factures[i][3])
        curs.execute(insert_stat, data)

    db.commit()
    db.close()


def test():
    all_fact = lire_tous(3)
    print(all_fact)
    print(trier(all_fact))
    print(maj_factures(all_fact))
    print("Totale prixTTC : ", total_TTC(all_fact))
    sauvgarderDansUnFichier(all_fact, 'factures.txt')
    sauvgarderDansUneBD(all_fact, 'factures.db')

test()