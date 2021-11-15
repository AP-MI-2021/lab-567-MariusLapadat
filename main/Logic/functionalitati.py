from Domain.cheltuiala import getNrApartament, getData, getSuma


def stergereToateCheltuielileDupaNrApartament(NrApartament, lista):
    """
    Sterge toate cheltuielile pentru un apartament dat
    :param NrApartament: numarul apartamentului ale carui cheltuieli sunt sterse
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cele ale apartamentului specificat
    """
    return [cheltuiala for cheltuiala in lista if getNrApartament(cheltuiala) != NrApartament]


def adunareValoareLaCheltuialaDinData(Data, Valoare, lista):
    """
    Adauga o valoare citita la toate cheltuielile din data citita
    :param Data:
    :param lista:
    :return: lista de cheltuieli la care se adauga o valoare citita la cheltuielile dintr-o data specifica
    """
    for cheltuiala in lista:
        if getData(cheltuiala) == Data:
            cheltuiala[2] = cheltuiala[2] + Valoare
    return lista


def ceaMaiMareCheltuiala(lista):
    """
    Determina cea mai mare cheltuiala pentru fiecare tip de cheltuiala
    :param lista:
    :return:
    """
    MaximTip1 = None
    MaximTip2 = None
    MaximTip3 = None
    for cheltuiala in lista:
        if cheltuiala[4] == "intretinere":
            if MaximTip1 is None or getSuma(cheltuiala) > MaximTip1:
                MaximTip1 = cheltuiala[0]
        if cheltuiala[4] == "canal":
            if MaximTip2 is None or getSuma(cheltuiala) > MaximTip2:
                MaximTip2 = cheltuiala[0]
        if cheltuiala[4] == "alte cheltuieli":
            if MaximTip1 is None or getSuma(cheltuiala) > MaximTip3:
                MaximTip3 = cheltuiala[0]
    return lista, (MaximTip1, MaximTip2, MaximTip3)
