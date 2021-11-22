from Tests.TestDomain import testCheltuiala
from Tests.testCRUD import testAdaugaCheltuiala, testStergereCheltuiala
from Tests.testFunctionalitati import testAdunareValoareLaCheltuialaDinData, testCeaMaiMareCheltuiala, \
    testOrdonareCheltuieliDescrescatorDupaSuma, testafisareSumeLunareApartamente, testUndoRedo


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergereCheltuiala()
    testAdunareValoareLaCheltuialaDinData()
    testCeaMaiMareCheltuiala()
    testOrdonareCheltuieliDescrescatorDupaSuma()
    testafisareSumeLunareApartamente()
    testUndoRedo()