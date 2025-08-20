def hipotenusa(cateto1, cateto2):
    return (cateto1**2 + cateto2**2) ** 0.5

c1 = float(input("Digite o primeiro cateto: "))
c2 = float(input("Digite o segundo cateto: "))

print(f"A hipotenusa é: {hipotenusa(c1, c2)}")