from Logic.CRUD import adaugaCheltuiala, stergereCheltuiala, modificareCheltuiala
from UI.console import showAll


def menu(lista):
    while True:
        try:
            comanda = input("Dati comanda: ")
            if comanda == "help":
                print("Pentru a adauga o noua cheltuiala folositi comanda add, iar apoi introduceti datele separate prin virgula")
                print("Exemplu: add,1,27,150,09.04.2000,canal")
                print("Pentru a sterge o cheltuiala folositi comanda delete si introduceti id-ul acesteia separat prin virgula")
                print("Exemplu: delete,1")
                print("Pentru a modifica o cheltuiala folositi comanda update si scrieti id-ul acesteia, urmat de noile date, separate prin virgula")
                print("Exemplu: update,1,27,350,09.04.2002,alte cheltuieli")
                print("Pentru a vedea toate cheltuielile folositi comanda showall")
                print("Pentru a iesi folositi comanda stop")
                print("Puteti folosi mai multe comenzi separandu-le prin ;")
                print("Exemplu: delete,1;showall")
            elif comanda == "stop":
                break
            else:
                comenzi = comanda.split(";")
                for i in range(len(comenzi)):
                    bucataComanda = comenzi[i].split(",")

                    if bucataComanda[0] == "add":
                        Id = bucataComanda[1]
                        NrApartament = bucataComanda[2]
                        Suma = bucataComanda[3]
                        Data = bucataComanda[4]
                        Tip = bucataComanda[5]

                        lista = adaugaCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)

                    elif bucataComanda[0] == "delete":
                        Id = bucataComanda[1]

                        lista = stergereCheltuiala(Id, lista)

                    elif bucataComanda[0] == "update":
                        Id = bucataComanda[1]
                        NrApartament = bucataComanda[2]
                        Suma = bucataComanda[3]
                        Data = bucataComanda[4]
                        Tip = bucataComanda[5]

                        lista = modificareCheltuiala(Id, NrApartament, Suma, Data, Tip, lista)

                    elif bucataComanda[0] == "showall":
                        showAll(lista)

                    else:
                        print("Comanda gresita! Reincercati!")

        except ValueError as ve:
            print("Eroare: {} ".format(ve))
