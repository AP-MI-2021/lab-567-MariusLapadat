def creeazaCheltuiala(Id, NrApartament, Suma, Data, Tip):
    """
    Creeaza un dictionar pentru cheltuiala
    :param id: string
    :param NrApartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :return:
    """
    return{
        "Id": Id,
        "NrApartament": NrApartament,
        "Suma": Suma,
        "Data": Data,
        "Tip": Tip

    }

def getId(cheltuiala):
    """
    ia id-ul unei cheltuieli
    :param cheltuiala: dictionar ce retine o cheltuiala
    :return: id-ul cheltuielii
    """
    return cheltuiala["Id"]

def getNrApartament(cheltuiala):
    """
    ia apartamentul unei cheltuieli
    :param cheltuiala: dictionar ce retine o cheltuiala
    :return: apartamentul cheltuielii
    """
    return cheltuiala["NrApartament"]

def getSuma(cheltuiala):
    """
    ia suma unei cheltuieli
    :param cheltuiala: dictionar ce retine o cheltuiala
    :return: suma cheltuielii
    """
    return cheltuiala["Suma"]

def getData(cheltuiala):
    """
    ia data unei cheltuieli
    :param cheltuiala: dictionar ce retine o cheltuiala
    :return: data cheltuielii
    """
    return cheltuiala["Data"]

def getTip(cheltuiala):
    """
    ia tip unei cheltuieli
    :param cheltuiala: dictionar ce retine o cheltuiala
    :return: id-ul cheltuielii
    """
    return cheltuiala["Tip"]

def toString(cheltuiala):
    return "Id: {}, NrApartament: {}, Suma: {}, Data: {}, Tip: {}".format(
        getId(cheltuiala),
        getNrApartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala),
    )