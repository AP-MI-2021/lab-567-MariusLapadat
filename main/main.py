from Tests.testAll import runAllTests
from UI.NewConsole import menu
from UI.console import runMenu


def main():
    runAllTests()
    lista=[]
    listaUndo=[]
    listaRedo=[]
    optiune=int(input("Meniul 1 sau 2: "))
    if optiune == 1:
        runMenu(lista,listaUndo,listaRedo)
    elif optiune == 2:
        lista=menu(lista)

main()
