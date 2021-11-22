from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergereCheltuiala, modificareCheltuiala
from Logic.functionalitati import stergereToateCheltuielileDupaNrApartament, adunareValoareLaCheltuialaDinData, \
    ceaMaiMareCheltuiala, ordonareCheltuieliDescrescatorDupaSuma, afisareSumeLunareApartamente


def printMenu(listaUndo,listaRedo):
    print("1. Adauga cheltuiala")
    print("2. Sterge cheltuiala")
    print("3. Modifica cheltuiala")
    print("4. Șterge toate cheltuielile pentru un apartament dat")
    print("5. Adunarea unei valori citite la toate cheltuielile dintr-o dată citită")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială")
    print("7. Ordonarea cheltuielilor descrescător după sumă")
    print("8. Afișarea sumelor lunare pentru fiecare apartament")
    print("a. Afiseaza toate cheltuielile")
    if len(listaUndo) > 0:
        print("u. Undo")
    if len(listaRedo) > 0:
        print("r. Redo")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista,listaUndo,listaRedo):
    try:
        Id = input("Dati id-ul: ")
        NrApartament = input("Dati apartamentul: ")
        Suma = float(input("Dati suma: "))
        Data = input("Dati data DD.MM.YYYY: ")
        Tip = input("Dati tip-ul: ")
        listaUndo.append(lista)
        listaRedo.clear()
        return adaugaCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeCheltuiala(lista,listaUndo,listaRedo):
    try:
        Id = input("Dati id-ul cheltuielii de sters: ")
        listaUndo.append(lista)
        listaRedo.clear()
        return stergereCheltuiala(Id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificareCheltuiala(lista,listaUndo,listaRedo):
    try:
        Id = input("Dati id-ul cheltuielii de modificat: ")
        NrApartament = input("Dati noul apartament: ")
        Suma = float(input("Dati noua suma: "))
        Data = input("Dati noua data DD.MM.YYYY: ")
        Tip = input("Dati noul tip: ")
        listaUndo.append(lista)
        listaRedo.clear()
        return modificareCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiStergereToateCheltuielileDupaNrApartament(lista,listaUndo,listaRedo):
    try:
        NrApartament = int(input("Dati numarul apartamentului caruia sa ii se stearga toate cheltuielile: "))
        listaUndo.append(lista)
        listaRedo.clear()
        return stergereToateCheltuielileDupaNrApartament(NrApartament, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiAdunareValoareLaCheltuialaDinData(lista,listaUndo,listaRedo):
    try:
        Data = input("Dati data sub format DD.MM.YYYY: ")
        Valoare = float(input("Dati valoarea de adaugat cheltuielilor: "))
        listaUndo.append(lista)
        listaRedo.clear()
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
    return lista


def uiOrdonareCheltuieliDescrescatorDupaSuma(lista,listaUndo,listaRedo):
    listaUndo.append(lista)
    listaRedo.clear()
    lista = ordonareCheltuieliDescrescatorDupaSuma(lista)
    return lista


def uiAfisareSumeLunareApartamente(lista):
    lista, rezultat = afisareSumeLunareApartamente(lista)
    for luna in rezultat:
        print("Luna {} are suma totala {}.".format(luna, rezultat[luna]))


def runMenu(lista,listaUndo,listaRedo):
    while True:
        printMenu(listaUndo,listaRedo)
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista,listaUndo,listaRedo)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista,listaUndo,listaRedo)
        elif optiune == "3":
            lista = uiModificareCheltuiala(lista,listaUndo,listaRedo)
        elif optiune == "4":
            lista = uiStergereToateCheltuielileDupaNrApartament(lista,listaUndo,listaRedo)
        elif optiune == "5":
            lista = uiAdunareValoareLaCheltuialaDinData(lista,listaUndo,listaRedo)
        elif optiune == "6":
            lista = uiCeaMaiMareCheltuiala(lista)
        elif optiune == "7":
            lista = uiOrdonareCheltuieliDescrescatorDupaSuma(lista,listaUndo,listaRedo)
        elif optiune == "8":
            lista = uiAfisareSumeLunareApartamente(lista)
        elif optiune == "u":
            if len(listaUndo) > 0:
                listaRedo.append(lista)
                lista = listaUndo.pop()
            else:
                print("Nu se poate face undo ")
        elif optiune == "r":
            if len(listaRedo) > 0:
                listaUndo.append(lista)
                lista = listaRedo.pop()
            else:
                print("Nu se poate face redo ")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
