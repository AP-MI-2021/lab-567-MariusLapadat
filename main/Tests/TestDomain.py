from Domain.cheltuiala import creeazaCheltuiala, getId, getNrApartament, getSuma, getData, getTip


def testCheltuiala():
    cheltuiala = creeazaCheltuiala("1", 27, 273.07, "09.04.2000", "canal")
    assert getId(cheltuiala) == "1"
    assert getNrApartament(cheltuiala) == 27
    assert getSuma(cheltuiala) == 273.07
    assert getData(cheltuiala) == "09.04.2000"
    assert getTip(cheltuiala) == "canal"
