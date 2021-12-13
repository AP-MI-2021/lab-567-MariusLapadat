from Domain.cheltuiala import getNrApartament, getData, getSuma, getId, getTip, creeazaCheltuiala
from Logic.CRUD import modificareCheltuiala, adaugaCheltuiala


def stergereToateCheltuielileDupaNrApartament(NrApartament, lista):
    """
    Sterge toate cheltuielile pentru un apartament dat
    :param NrApartament: numarul apartamentului ale carui cheltuieli sunt sterse
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cele ale apartamentului specificat
    """
    listaNoua = []
    for cheltuiala in lista:
        print(getNrApartament(cheltuiala))
        if getNrApartament(cheltuiala) == NrApartament:
            listaNoua.append(cheltuiala)
    return listaNoua


def adunareValoareLaCheltuialaDinData(Data, Valoare, lista):
    """
    Adauga o valoare citita la toate cheltuielile din data citita
    :param Data:
    :param lista:
    :return: lista de cheltuieli la care se adauga o valoare citita la cheltuielile dintr-o data specifica
    """
    listaNoua=[]
    for cheltuiala in lista:
        if getData(cheltuiala) != Data:
            listaNoua.append(cheltuiala)
        else:
            listaNoua.append(creeazaCheltuiala(getId(cheltuiala),getNrApartament(cheltuiala),getSuma(cheltuiala)+Valoare,getData(cheltuiala),getTip(cheltuiala)))
    return listaNoua


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


def ordonareCheltuieliDescrescatorDupaSuma(lista):
    """
    Ordoneaza cheltuielile descrescator dupa suma
    :param lista:
    :return:
    """
    return sorted(lista, key=getSuma, reverse=True)


def afisareSumeLunareApartamente(lista):
    """
    Afișeaza sumele lunare pentru fiecare apartament
    :param lista:
    :return:
    """
    rezultat = {}
    for cheltuiala in lista:
        data = getData(cheltuiala).split(".")[1]
        pret = getSuma(cheltuiala)
        if data in rezultat:
            rezultat[data] = rezultat[data] + pret
        else:
            rezultat[data] = pret
    return lista, rezultat
