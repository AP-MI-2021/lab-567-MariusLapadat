from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergereCheltuiala, modificareCheltuiala
from Logic.functionalitati import stergereToateCheltuielileDupaNrApartament


def printMenu():
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Șterge toate cheltuielile pentru un apartament dat")
    print("a. Afiseaza toate cheltuielile")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    Id = input("Dati id-ul: ")
    NrApartament = input("Dati apartamentul: ")
    Suma = float(input("Dati suma: "))
    Data = input("Dati data DD.MM.YYYY: ")
    Tip = input("Dati tip-ul: ")
    return adaugaCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)


def uiStergeCheltuiala(lista):
    Id = input("Dati id-ul cheltuielii de sters: ")
    return stergereCheltuiala(Id, lista)


def uiModificareCheltuiala(lista):
    Id = input("Dati id-ul cheltuielii de modificat: ")
    NrApartament = input("Dati noul apartament: ")
    Suma = float(input("Dati noua suma: "))
    Data = input("Dati noua data DD.MM.YYYY: ")
    Tip = input("Dati noul tip: ")
    return modificareCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiStergereToateCheltuielileDupaNrApartament(lista):
    NrApartament = int(input("Dati numarul apartamentului caruia sa ii se stearga toate cheltuielile: "))
    return stergereToateCheltuielileDupaNrApartament(NrApartament, lista)


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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
