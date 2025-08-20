import math
def calcular_imc(altura, peso):
    return peso / (altura ** 2)
altura = float(input("digite sua altura"))
peso = float(input("diite seu peso"))
print("seu massa corporal é: ", calcular_imc(altura , peso))
