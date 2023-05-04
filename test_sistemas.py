import unittest
from hexadecimal import Hexadecimal
from octal import Octal
from binario import Binario
from decimal import Decimal


class TestSistemaHexadecimal(unittest.TestCase):

    #! HEXADECIMAL A BINARIO

    def testHexadecimalABinario(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalABinario('FF')
        self.assertEqual(result, '11111111')

    def testHexadecimalABinario_II(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalABinario('81D')
        self.assertEqual(result, '100000011101')
    
    def testHexadecimalABinario_III(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalABinario('17E')
        self.assertEqual(result, '000101111110')

    #! HEXADECIMAL A OCTAL

    def testHexadecimalAOctal(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalAOctal('6F5')
        self.assertEqual(result, 3365)

    def testHexadecimalAOctal_II(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalAOctal('81D')
        self.assertEqual(result, 4035)

    def testHexadecimalAOctal_III(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalAOctal('7D1')
        self.assertEqual(result, 3721)

    #! HEXADECIMAL A DECIMAL

    def testHexadecimalADecimal(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalADecimal('3E')
        self.assertEqual(result, 62)

    def testHexadecimalADecimal_II(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalADecimal('81D')
        self.assertEqual(result, 2077)

    def testHexadecimalADecimal_III(self):
        hexa = Hexadecimal()
        result = hexa.HexadecimalADecimal('7D1')
        self.assertEqual(result, 2001)


class TestSistemaOctal(unittest.TestCase):

    #! OCTAL A DECIMAL

    def testOctalADecimal(self):
        oc = Octal()
        result = oc.OctalADecimal(412)
        self.assertEqual(result, 266)

    def testOctalADecimal_II(self):
        oc = Octal()
        result = oc.OctalADecimal(572)
        self.assertEqual(result, 378)

    def testOctalADecimal_III(self):
        oc = Octal()
        result = oc.OctalADecimal(2077)
        self.assertEqual(result, 1087)

    #! OCTAL A BINARIO

    def testOctalABinario(self):
        oc = Octal()
        result = oc.OctalABinario(7654)
        self.assertEqual(result, '111110101100')

    def testOctalABinario_II(self):
        oc = Octal()
        result = oc.OctalABinario(2077)
        self.assertEqual(result, '010000111111')

    def testOctalABinario_III(self):
        oc = Octal()
        result = oc.OctalABinario(17)
        self.assertEqual(result, '001111')

    #! OCTAL A HEXADECIMAL

    def testOctalAHexadecimal(self):
        oc = Octal()
        result = oc.OctalAHexadecimal(2077)
        self.assertEqual(result, '43F')

    def testOctalAHexadecimal_II(self):
        oc = Octal()
        result = oc.OctalAHexadecimal(17)
        self.assertEqual(result, 'F')

    def testOctalAHexadecimal_III(self):
        oc = Octal()
        result = oc.OctalAHexadecimal(2001)
        self.assertEqual(result, '401')



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

    def testBinarioAHexadecimal_IV(self):
        bin = Binario()
        result = bin.binarioAHexadecimal('001111')
        self.assertEqual(result, 'F')
    
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

class TestSistemaBinario(unittest.TestCase):

    #! DECIMAL A BINARIO
    def testDecimalABinario(self):
        deci = Decimal()
        result = deci.decimalABinario(36)
        self.assertEqual(result, '100100')

    def testDecimalABinario_II(self):
        deci = Decimal()
        result = deci.decimalABinario(2077)
        self.assertEqual(result, '100000011101')

    def testDecimalABinario_III(self):
        deci = Decimal()
        result = deci.decimalABinario(144)
        self.assertEqual(result, '10010000')




if __name__ == '__main__':
    unittest.main()