from Domain.cheltuiala import getId, getNrApartament, getData, getSuma, getTip
from Logic.CRUD import adaugaCheltuiala, getById, stergereCheltuiala


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 27, 273.07, "09.04.2000", "canal",lista)

    assert len(lista) == 1
    assert getId(getById("1",lista)) == "1"
    assert getNrApartament(getById("1",lista)) == 27
    assert getSuma(getById("1",lista)) == 273.07
    assert getData(getById("1",lista)) == "09.04.2000"
    assert getTip(getById("1",lista)) == "canal"


def testStergereCheltuiala():
    lista=[]
    lista = adaugaCheltuiala("1", 27, 273.07, "09.04.2000", "canal", lista)
    lista = adaugaCheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)

    lista = stergereCheltuiala("1", lista)
    assert len(lista)==1
    assert getById("1",lista) is None
    assert getById("2",lista) is not None

    lista = stergereCheltuiala("3", lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None