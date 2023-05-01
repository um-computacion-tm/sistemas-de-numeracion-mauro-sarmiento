import unittest
from hexadecimal import Hexadecimal
from octal import Octal
from binario import Binario
from decimal import Decimal

class TestSistemaBinario(unittest.TestCase):

    #! BINARIO A DECIMAL

    def testBinarioADecimal(self):
        bin = Binario()
        result = bin.binarioADecimal('1010011')
        self.assertEqual(result, 83)

    def testBinarioADecimal_II(self):
        bin = Binario()
        result = bin.binarioADecimal('10110')
        self.assertEqual(result, 22)

    def testBinarioADecimal_III(self):
        bin = Binario()
        result = bin.binarioADecimal('11010011010')
        self.assertEqual(result, 1690)
    
    #! BINARIO A HEXADECIMAL

    def testBinarioAHexadecimal(self):
        bin = Binario()
        result = bin.binarioAHexadecimal('11110111')
        self.assertEqual(result, 'F7')

    def testBinarioAHexadecimal_II(self):
        bin = Binario()
        result = bin.binarioAHexadecimal('100000000100')
        self.assertEqual(result, '804')

    def testBinarioAHexadecimal_III(self):
        bin = Binario()
        result = bin.binarioAHexadecimal('10110010111')
        self.assertEqual(result, '597')
    
    #! BINARIO A OCTAL

    def testBinarioAOctal(self):
        bin = Binario()
        result = bin.binarioAOctal('110010')
        self.assertEqual(result, 62)

    def testBinarioAOctal_II(self):
        bin = Binario()
        result = bin.binarioAOctal('111101111')
        self.assertEqual(result, 757)

    def testBinarioAOctal_III(self):
        bin = Binario()
        result = bin.binarioAOctal('10011011')
        self.assertEqual(result, 233)

    


if __name__ == '__main__':
    unittest.main()