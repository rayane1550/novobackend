import math

def area_circulo():
    raio = float(input("Digite o valor do raio do círculo: "))
    area = math.pi * raio ** 2
    print(f"A área do círculo é: {area}")

area_circulo()
