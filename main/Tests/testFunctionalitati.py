from Domain.cheltuiala import creeazaCheltuiala, getSuma, getId
from Logic.CRUD import adaugaCheltuiala
from Logic.functionalitati import adunareValoareLaCheltuialaDinData, ceaMaiMareCheltuiala, \
    ordonareCheltuieliDescrescatorDupaSuma, afisareSumeLunareApartamente


def testAdunareValoareLaCheltuialaDinData():
    lista = []
    lista = adaugaCheltuiala("1", 27, 150, "09.04.2000", "canal", lista)
    lista = adaugaCheltuiala("2", 30, 50, "03.04.2002", "alte cheltuieli", lista)
    lista = adaugaCheltuiala("3", 31, 100, "05.04.2003", "intretinere", lista)

    lista = adunareValoareLaCheltuialaDinData("09.04.2000", 100, lista)
    assert getSuma(lista[0]) == 250
    assert getSuma(lista[1]) == 50
    assert getSuma(lista[2]) == 100


def testCeaMaiMareCheltuiala():
    lista1 = []
    lista1 = adaugaCheltuiala("1", 27, 150, "09.04.2000", "canal", lista1)
    lista1 = adaugaCheltuiala("2", 30, 50, "03.04.2002", "alte cheltuieli", lista1)
    lista1 = adaugaCheltuiala("3", 31, 100, "05.04.2003", "intretinere", lista1)

    lista1, tuplu = ceaMaiMareCheltuiala(lista1)
    assert tuplu[0] == "3"
    assert tuplu[1] == "1"
    assert tuplu[2] == "2"


def testOrdonareCheltuieliDescrescatorDupaSuma():
    lista2 = []
    lista2 = adaugaCheltuiala("1", 27, 150, "09.04.2000", "canal", lista2)
    lista2 = adaugaCheltuiala("2", 30, 50, "03.04.2002", "alte cheltuieli", lista2)
    lista2 = adaugaCheltuiala("3", 31, 100, "05.04.2003", "intretinere", lista2)

    lista2 = ordonareCheltuieliDescrescatorDupaSuma(lista2)
    assert getId(lista2[0]) == "1"
    assert getId(lista2[1]) == "3"
    assert getId(lista2[2]) == "2"


def testafisareSumeLunareApartamente():
    lista3 = []
    lista3 = adaugaCheltuiala("1", 27, 150, "09.04.2000", "canal", lista3)
    lista3 = adaugaCheltuiala("2", 30, 50, "03.04.2002", "alte cheltuieli", lista3)
    lista3 = adaugaCheltuiala("3", 31, 100, "05.04.2003", "intretinere", lista3)
    lista3 = adaugaCheltuiala("4", 25, 200, "05.07.2003", "intretinere", lista3)
    lista3 = adaugaCheltuiala("5", 20, 50, "20.04.2003", "intretinere", lista3)

    lista3, rezultat = afisareSumeLunareApartamente(lista3)
    assert rezultat['04'] == 350
    assert rezultat['07'] == 200


def testUndoRedo():
    lista4 = []
    listaUndo1 = []
    listaRedo1 = []

    listaUndo1.append(lista4)
    lista4 = adaugaCheltuiala("1", 27, 150, "09.04.2000", "canal", lista4)

    listaUndo1.append(lista4)
    lista4 = adaugaCheltuiala("2", 25, 200, "05.07.2003", "intretinere", lista4)

    listaUndo1.append(lista4)
    lista4 = adaugaCheltuiala("3", 20, 50, "20.04.2003", "intretinere", lista4)

    assert getId(lista4[0]) == "1"
    assert getId(lista4[1]) == "2"
    assert getId(lista4[2]) == "3"

    listaRedo1.append(lista4)
    lista4 = listaUndo1.pop()
    assert len(lista4) == 2
    assert listaUndo1 == [[], [["1", 27, 150, "09.04.2000", "canal"]]]

    listaRedo1.append(lista4)
    lista4 = listaUndo1.pop()
    assert len(lista4) == 1
    assert listaUndo1 == [[]]

    listaUndo1.append(lista4)
    lista4 = listaRedo1.pop()
    assert len(lista4) == 2
