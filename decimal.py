
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
        deci_hexa = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8'
                , 9:'9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        numero_hexadecimal = ''
        hexadecimales = []
        while numero_decimal > 15:
            resto = numero_decimal % 16
            hexadecimales.append(resto)
            numero_decimal = numero_decimal // 16
        hexadecimales.append(numero_decimal)
        for i in range(len(hexadecimales)):
            div = hexadecimales[i]
            if div in deci_hexa:
                numero_hexadecimal += deci_hexa[div]
        numero_hexadecimal = numero_hexadecimal[::-1]
        return numero_hexadecimal



    def decimalAOctal(self, numero_decimal):
        numero_octal = ''
        octales = []
        while numero_decimal > 8:
            resto = numero_decimal % 8
            octales.append(resto)
            numero_decimal = numero_decimal // 8
        octales.append(numero_decimal)
        for i in range(len(octales)):
            numero_octal += str(octales[i])
        numero_octal = numero_octal[::-1]
        return numero_octal
    