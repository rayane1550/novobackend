def numero_digitados(numero):
    if numero < 0:
        return "Número inválido. Por favor, insira um número inteiro positivo."
    
    digitos = str(numero)
    return len(digitos)
numero = int(input("Digite um número inteiro positivo: "))
print(f"O número de dígitos em {numero} é: {numero_digitados(numero)}")