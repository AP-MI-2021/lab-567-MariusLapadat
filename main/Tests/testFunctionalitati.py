from Domain.cheltuiala import creeazaCheltuiala, getSuma
from Logic.CRUD import adaugaCheltuiala
from Logic.functionalitati import adunareValoareLaCheltuialaDinData, ceaMaiMareCheltuiala


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
