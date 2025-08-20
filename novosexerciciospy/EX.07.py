import math

def volume_cilindro(raio, altura):
    return math.pi * raio ** 2 * altura

raio = float(input("Digite o valor do raio do cilindro: "))
altura = float(input("Digite o valor da altura do cilindro: "))

print(f"O volume do cilindro é: {volume_cilindro(raio, altura)}")