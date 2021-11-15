from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergereCheltuiala, modificareCheltuiala
from Logic.functionalitati import stergereToateCheltuielileDupaNrApartament, adunareValoareLaCheltuialaDinData, \
    ceaMaiMareCheltuiala


def printMenu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Șterge toate cheltuielile pentru un apartament dat")
    print("5. Adunarea unei valori citite la toate cheltuielile dintr-o dată citită")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială")
    print("a. Afiseaza toate cheltuielile")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    try:
        Id = input("Dati id-ul: ")
        NrApartament = input("Dati apartamentul: ")
        Suma = float(input("Dati suma: "))
        Data = input("Dati data DD.MM.YYYY: ")
        Tip = input("Dati tip-ul: ")
        return adaugaCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeCheltuiala(lista):
    Id = input("Dati id-ul cheltuielii de sters: ")
    return stergereCheltuiala(Id, lista)


def uiModificareCheltuiala(lista):
    try:
        Id = input("Dati id-ul cheltuielii de modificat: ")
        NrApartament = input("Dati noul apartament: ")
        Suma = float(input("Dati noua suma: "))
        Data = input("Dati noua data DD.MM.YYYY: ")
        Tip = input("Dati noul tip: ")
        return modificareCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiStergereToateCheltuielileDupaNrApartament(lista):
    try:
        NrApartament = int(input("Dati numarul apartamentului caruia sa ii se stearga toate cheltuielile: "))
        return stergereToateCheltuielileDupaNrApartament(NrApartament, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiAdunareValoareLaCheltuialaDinData(lista):
    try:
        Data = input("Dati data sub format DD.MM.YYYY: ")
        Valoare = float(input("Dati valoarea de adaugat cheltuielilor: "))
        return adunareValoareLaCheltuialaDinData(Data, Valoare, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiCeaMaiMareCheltuiala(lista):
    lista, tuplu = ceaMaiMareCheltuiala(lista)
    if tuplu[0] is None:
        print("Nu avem cheltuieli de tip întreținere")
    else:
        print("Cea mai mare cheltuiala de tip întreținere are ID-ul: ", tuplu[0])
    if tuplu[1] is None:
        print("Nu avem cheltuieli de tip canal")
    else:
        print("Cea mai mare cheltuiala de tip canal are ID-ul: ", tuplu[1])
    if tuplu[2] is None:
        print("Nu avem cheltuieli de tip alte cheltuieli")
    else:
        print("Cea mai mare cheltuiala de tip alte cheltuieli are ID-ul: ", tuplu[2])


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista)
        elif optiune == "3":
            lista = uiModificareCheltuiala(lista)
        elif optiune == "4":
            lista = uiStergereToateCheltuielileDupaNrApartament(lista)
        elif optiune == "5":
            lista = uiAdunareValoareLaCheltuialaDinData(lista)
        elif optiune == "6":
            lista = uiCeaMaiMareCheltuiala(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
