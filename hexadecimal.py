
class Hexadecimal:
    def HexadecimalADecimal(self, numero_hexadecimal):
        pass

    def HexadecimalAOctal(self, numero_hexadecimal):
        pass

    def HexadecimalABinario(self, numero_hexadecimal):
        numero_hexadecimal = str(numero_hexadecimal)
        binario_hexa = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000'
                , '9': '1001', 'A':'1010', 'B': '1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
        num_bin = ''
        for i in range(len(numero_hexadecimal)):
            div = numero_hexadecimal[i]
            if div in binario_hexa:
                num_bin += str(binario_hexa[div])
        return (num_bin)
