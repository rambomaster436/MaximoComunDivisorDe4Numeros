import unittest

def MCD2N(nro1, nro2):
    while nro2:
        nro1, nro2 = nro2, nro1 % nro2
    return nro1

def MCD4N(nro1, nro2, nro3, nro4):
    mcd12 = MCD2N(nro1, nro2)
    mcd123 = MCD2N(mcd12, nro3)
    return MCD2N(mcd123, nro4)

class TestOperaciones(unittest.TestCase):
    
    def test_MCD_2N(self):
        esperado = 5
        actual = MCD2N(15, 10)
        self.assertEqual(actual, esperado)

    def test_MCD_4N(self):
        esperado = 5
        actual = MCD4N(15, 10, 25, 35)
        self.assertEqual(actual, esperado)

if __name__ == '__main__':
    unittest.main()
