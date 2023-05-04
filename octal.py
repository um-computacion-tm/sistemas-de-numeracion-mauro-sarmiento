
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
    
    def OctalAHexadecimal(self, numero_octal):
        pass

    def OctalABinario(self, numero_octal):
        pass