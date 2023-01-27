class Calculator:
    def saberi(self, a, b):
        return a + b
calc = Calculator()
#broj1, broj2, ocekivano, dobijeno
broj1 = 2
broj2 = 3
ocekivano = broj1 + broj2 # 5

dobijeno = calc.saberi(broj1, broj2)

print(ocekivano == dobijeno)


import unittest

class TestKalkulator(unittest.TestCase):
    def test_sabiranje(self):
        kalkulator = Calculator()
        ocekivano = 5
        dobijeno = kalkulator.saberi(2, 3)

        self.assertEqual(ocekivano, dobijeno)

unittest.main()