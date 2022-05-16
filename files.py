"""
    Fichier Texte
"""
"""
f = open("file.txt", "r+")
print(f.readlines())
f.write("********Aymen*********")
f = open("file.txt", "r")
for line in f:
    print(line+"\n")

f.close()
"""

"""
    Fichier Binaire
"""
import pickle

def readBinFile():
    f = open("venv/ficheBib.bin", "rb")
    data = pickle.load(f)
    f.close()
    print(data)

def writeBinFile():
    f = open("venv/ficheBib.bin", "wr")
    x = [1, 2, 3, 4]
    pickle.dump(x, f)
    f.close()

"""***************************"""
def write():
    file = open("venv/ficheBib.bin", "wb+")
    records = []
    x = 1
    while x==1:
        no = int(input("Enter enrolled NO"))
        name = input("Enter your Name")
        age = int(input("Enter Your Age"))
        data = [no, name, age]
        records.append(data)
        ch = input("do you Want to add more record")
        if ch == 'n':
            break
    pickle.dump(records, file)
    file.close()

def read():
    f = open("venv/f.dat", "rb")
    f.seek(0)
    data = pickle.load(f)
    for i in data:
        print(i)
read()
















