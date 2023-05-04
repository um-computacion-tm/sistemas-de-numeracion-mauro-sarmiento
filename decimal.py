
class Decimal:
    def decimalABinario(self, numero_decimal):
        numero_binario = ''
        binarios = []
        binarios.append(numero_decimal)
        while numero_decimal > 2:
            par_impar = numero_decimal // 2
            binarios.append(par_impar)
            numero_decimal = numero_decimal / 2
        for i in binarios:
            if (i % 2) != 0:
                numero_binario += '1'
            elif (i % 2) == 0:
                numero_binario += '0'
        numero_binario = numero_binario[::-1]
        return numero_binario

    def decimalAHexadecimal(self, numero_decimal):
        pass

    def decimalAOctal(self, numero_decimal):
        pass