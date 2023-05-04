from binario import Binario

class Octal:
    def OctalADecimal(self, numero_octal):
        numero_octal = str(numero_octal)
        decimal_list = []
        decimal = 0
        base = len(numero_octal) - 1
        for k in range(len(numero_octal)):
            base_num = 8**base
            decimal_list.append(base_num)
            base -= 1
        for i in range(len(decimal_list)):
            value = decimal_list[i] * int(numero_octal[i])
            decimal += value
        return decimal
    
    def OctalABinario(self, numero_octal):
        numero_octal = str(numero_octal)
        binario_octal = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'}
        num_bin = ''
        for i in range(len(numero_octal)):
            div = int(numero_octal[i])
            if div in binario_octal:
                num_bin += str(binario_octal[div])
        return (num_bin)


    def OctalAHexadecimal(self, numero_octal):
        numero_octal = str(numero_octal)
        bin = Binario()
        octo = Octal().OctalABinario(numero_octal)
        hexa = bin.binarioAHexadecimal(octo)
        return hexa

