from Domain.cheltuiala import getNrApartament


def stergereToateCheltuielileDupaNrApartament(NrApartament,lista):
    """
    Sterge toate cheltuielile pentru un apartament dat
    :param NrApartament: numarul apartamentului ale carui cheltuieli sunt sterse
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cele ale apartamentului specificat
    """
    return [cheltuiala for cheltuiala in lista if getNrApartament(cheltuiala) != NrApartament]
