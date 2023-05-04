
class Binario:
    def binarioADecimal(self, numero_binario):
        numero_binario = str(numero_binario)
        decimal_list = []
        decimal = 0
        base = len(numero_binario) - 1
        for k in range(len(numero_binario)):
            base_num = 2**base
            decimal_list.append(base_num)
            base -= 1
        for i in range(len(decimal_list)):
            value = decimal_list[i] * int(numero_binario[i])
            decimal += value
        return decimal


    def binarioAHexadecimal(self, numero_binario):
        numero_binario = str(numero_binario)
        for k in range(len(numero_binario)):
            if (len(numero_binario) % 4) != 0:
                numero_binario = '0' + numero_binario
        binario = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, '0100': 4, '0101': 5, '0110': 6, '0111': 7, '1000': 8
                , '1001': 9, '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        hexadecimal = ''
        for i in range(0, len(numero_binario), 4):
            division = numero_binario[i:i+4]
            if division in binario:
                hexadecimal += str(binario[division])
        if hexadecimal[0] == '0':
            hexadecimal = hexadecimal[1:]
        return hexadecimal


    def binarioAOctal(self, numero_binario):
        numero_binario = str(numero_binario)
        for k in range(len(numero_binario)):
            if (len(numero_binario) % 3) != 0:
                numero_binario = '0' + numero_binario
        binario = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
        octal = ''
        for i in range(0, len(numero_binario), 3):
            division = numero_binario[i:i+3]
            if division in binario:
                octal += str(binario[division])
        return int(octal)


