from Tests.TestDomain import testCheltuiala
from Tests.testCRUD import testAdaugaCheltuiala, testStergereCheltuiala
from Tests.testFunctionalitati import testAdunareValoareLaCheltuialaDinData, testCeaMaiMareCheltuiala


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergereCheltuiala()
    testAdunareValoareLaCheltuialaDinData()
    testCeaMaiMareCheltuiala()