import math
def raio_circulo(area):
    if area < 0:
        return "Área inválida. Por favor, insira um valor positivo."
    
    raio = math.sqrt(area / math.pi)
    return raio
area = float(input("Digite a área do círculo: "))
print(f"O raio do círculo é: {raio_circulo(area)}")