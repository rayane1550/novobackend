import math

def decimal_para_binario(n):
    if n == 0: 
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario

numero_decimal = int(input("Digite um número decimal: "))
print("O numero decimal é:", numero_decimal)
print("O número binário é:", decimal_para_binario(numero_decimal))

