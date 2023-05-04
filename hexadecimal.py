from binario import Binario

class Hexadecimal:
    def HexadecimalADecimal(self, numero_hexadecimal):
        numero_hexadecimal = str(numero_hexadecimal)
        deci_hexa = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8
                , '9': 9, 'A':10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        decimal_list = []
        decimal = 0
        base = len(numero_hexadecimal) - 1
        for k in range(len(numero_hexadecimal)):
            base_num = 16**base
            decimal_list.append(base_num)
            base -= 1
        for i in range(len(decimal_list)):
            div = numero_hexadecimal[i]
            if div in deci_hexa:
                value = decimal_list[i] * deci_hexa[div]
                decimal += value
        return decimal

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

    def HexadecimalAOctal(self, numero_hexadecimal):
        numero_hexadecimal = str(numero_hexadecimal)
        hexa = Hexadecimal().HexadecimalABinario(numero_hexadecimal)
        bina = Binario().binarioAOctal(hexa)
        return bina

    
