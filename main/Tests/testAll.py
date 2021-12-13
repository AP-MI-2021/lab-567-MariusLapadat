from Tests.TestDomain import testCheltuiala
from Tests.testCRUD import testAdaugaCheltuiala, testStergereCheltuiala
from Tests.testFunctionalitati import testCeaMaiMareCheltuiala, \
    testOrdonareCheltuieliDescrescatorDupaSuma, testafisareSumeLunareApartamente, testUndoRedo, \
    testAdunareValoareLaCheltuialaDinData


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergereCheltuiala()
    testAdunareValoareLaCheltuialaDinData()
    testCeaMaiMareCheltuiala()
    testOrdonareCheltuieliDescrescatorDupaSuma()
    testafisareSumeLunareApartamente()
    testUndoRedo()
