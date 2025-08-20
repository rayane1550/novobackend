def bonario_para_decimal(binario):
    numero = binario[::-1]
    potencial = 0
    soma = 0
    for i in numero:
        soma += int(i) * (2 ** potencial)
        potencial += 1
    return soma

binario = input("Digite um número binário: ")
print("O número decimal é:", bonario_para_decimal(binario))