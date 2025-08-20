import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 10

    for tentativa in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}/{tentativas} - Escolha um número de 1 a 100: "))
        if palpite < 1 or palpite > 100:
            print("número fora do intervalo. Tente novamente")
            continue
        if palpite == numero_secreto:
            print("você acertou, parabéns")
            break
        elif palpite < numero_secreto:
            print("o número secreto é maior")
        else:
            print("o número secreto é menor")
    else:
        print(f"você perdeu, tente novamente. O número era {numero_secreto}.")

jogo_adivinhacao()
       


