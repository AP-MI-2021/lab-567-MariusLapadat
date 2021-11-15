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
    if getById(Id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if Data.count('.') != 2 or Data.split(".")[0].isnumeric() == False or Data.split(".")[1].isnumeric() == False or \
            Data.split(".")[2].isnumeric() == False:
        raise ValueError("Ati bagat data gresita!")
    else:
        if (Data.split(".")[1] == "01" or Data.split(".")[1] == "03" or Data.split(".")[1] == "05" or Data.split(".")[
            1] == "07" or Data.split(".")[1] == "08" or Data.split(".")[1] == "10" or Data.split(".")[
                1] == "12") and int(Data.split(".")[0]) > 31:
            raise ValueError("Ati bagat data gresita!")
        if (Data.split(".")[1] == "04" or Data.split(".")[1] == "06" or Data.split(".")[1] == "09" or Data.split(".")[
            1] == "11") and int(Data.split(".")[0]) > 30:
            raise ValueError("Ati bagat data gresita!")
        if Data.split(".")[1] == "02" and int(Data.split(".")[2]) % 4 == 0 and int(Data.split(".")[0]) > 29:
            raise ValueError("Ati bagat data gresita!")
        if Data.split(".")[1] == "02" and int(Data.split(".")[2]) % 4 != 0 and int(Data.split(".")[0]) > 28:
            raise ValueError("Ati bagat data gresita!")
        if int(Data.split(".")[1]) > 12:
            raise ValueError("Ati bagat data gresita!")
    if Tip != "canal" and Tip != "intretinere" and Tip != "alte cheltuieli":
        raise ValueError("Ati bagat tip-ul gresit")

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
