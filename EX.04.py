import math
def distancia_pontos(X1, y1, x2, y2 ):
    return math.sqrt((x2 - x1 )**2 + (y2 - y1)**2)
x1 = int(input("digite a cordenada x do primeiro ponto: "))
y1 = int(input("digite a cordenada y do primeiro ponto: "))
x2 = int(input("diite a cordenada x do segundo ponto: "))
y2 = int(input("digite a cordenada y do segundo pontoo: "))
print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é: {distancia_pontos(x1, y1, x2, y2)}")

    