import random
def gerar_numero_aleatorio(m, n):
    if n > m:
        numero_aleatorio = random.randint(m, n)
    else:
        numero_aleatorio = random.randint(n, m)
    return numero_aleatorio
m = int(input("Digite o valor n: "))
n = int(input("Digite o valor m: "))
print(f"O número aleatório gerado entre {m} e {n} é: {gerar_numero_aleatorio(m, n)}")