from Domain.cheltuiala import creeazaCheltuiala, getId


def adaugaCheltuiala(Id, NrApartament, Suma, Data, Tip, lista):
    """
    adauga o cheltuiala in lista
    :param Id:
    :param NrApartament:
    :param Suma:
    :param Data:
    :param Tip:
    :param lista: lista cu cheltuieli
    :return: o lista cu toate cheltuielile vechi plus una noua
    """
    cheltuiala = creeazaCheltuiala(Id, NrApartament, Suma, Data, Tip)
    return lista + [cheltuiala]


def getById(id, lista):
    """
    da elementul din lista cu un id dat
    :param id:
    :param lista:
    :return: cheltuiala cu id-ul dat sau None, daca nu exista cheltuiala cu id-ul dat
    """
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            return cheltuiala
    return None


def stergereCheltuiala(Id, lista):
    """
    Sterge o cheltuiala din lista de cheltuieli
    :param Id:
    :param lista:
    :return: o lista de cheltuieli fara cheltuiala cu id-ul specificat
    """
    return [cheltuiala for cheltuiala in lista if getId(cheltuiala) != Id]


def modificareCheltuiala(Id, NrApartament, Suma, Data, Tip, lista):
    """

    :param Id:
    :param NrApartament:
    :param Suma:
    :param Data:
    :param Tip:
    :param lista:
    :return:
    """
    listaNoua = []
    for cheltuiala in lista:
        if getId(cheltuiala) == Id:
            cheltuialaNoua = creeazaCheltuiala(Id, NrApartament, Suma, Data, Tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
