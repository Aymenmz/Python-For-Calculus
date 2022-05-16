from sqlite3 import *


def afficher(database, req):
    database = connect(database)
    cur = database.cursor()
    res = cur.execute(req)
    for line in res:
        print(line)
    database.close()


def enregisterFile(database, req, file):
    database = connect(database)
    file = open(file, "w")
    cur = database.cursor()
    res = cur.execute(req)
    for line in res:
        file.write(str(line) + '\n')
    database.close()
    file.close()


def enregisterVue(database, req, VUE):
    database = connect(database)
    cur = database.cursor()
    requete = "Create view " + VUE + "as " + req
    cur.execute(requete)
    database.close()


def statistique(database, file):
    database = connect(database)
    cur = database.cursor()
    f = open(file, 'w')
    nbr_candidats = cur.execute('''select count(no) from etudiant''')
    listeAdmis = cur.execute('''select name from etudiant where note>=10''')
    nbrNotAdmis = cur.execute('''select count(no) from etudiant where note<10''')
    maxNote = cur.execute('''select max(note) from etudiant''')
    minNote = cur.execute('''select min(note) from etudiant''')
    f.write('la nombre des Candidates : ' + str(nbr_candidats.fetchone()) + ' \n')
    f.write('les Candidates Admis : ' + str(listeAdmis.fetchone()) + ' \n')
    f.write('le nombre de candidates non admis : ' + str(nbrNotAdmis.fetchone()) + ' \n')
    f.write('la note maximal est : ' + str(maxNote.fetchone()))
    f.write('la note minimal est : ' + str(minNote.fetchone()))
    database.close()
    f.close()


db = input("Enter le nom de la base de données : ")
req = input("Enter la requete : ")
file = input("Enter le nom de fichier : ")

afficher(db, req)
enregisterFile(db, req, "file.txt")
statistique(db, file)
