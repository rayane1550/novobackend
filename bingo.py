import random
import pyttsx3
from pyfiglet import figlet_format
import time


class Bingo:
    def __init__(self):
        # Guarda os numeros que já foram sorteados (Ex: "B14", "G50")
        self.numeros_sorteados = set()
        # Mapeamento das letras para seus respectivos intervalos
        self.ranges = {
            'B': (1, 15),
            'I': (16, 30),
            'N': (31, 45),
            'G': (46, 60),
            'O': (61, 75)
        }
   
    # Sorteia e retorna uma letra entre ('B','I','N','G','O')
    def sortear_letra(self):
        letra = random.choice(list(self.ranges.keys()))
        return letra


    # Dado uma letra, sortear e retornar um número possível
    def sortear_numero(self, letra):
        min_val, max_val = self.ranges[letra]
        return random.randint(min_val, max_val)


    # Sorteia uma combinação única de letra e número
    def sortear(self):
        if len(self.numeros_sorteados) == 75:
            return "FIM DE JOGO! Todas as pedras foram sorteadas."


        while True:
            letra = self.sortear_letra()
            numero = self.sortear_numero(letra)
            sorteio_str = f"{letra}{numero}"
            if sorteio_str not in self.numeros_sorteados:
                self.numeros_sorteados.add(sorteio_str)
                return sorteio_str


    def jogar(self):
        print(figlet_format("BINGO", font="standard"))
        print("Iniciando o sorteio automático a cada 10 segundos...")


        while True:
            print("\nSorteando em 3")
            time.sleep(1)
            print("Sorteando em 2")
            time.sleep(1)
            print("Sorteando em 1")
            time.sleep(1)


            sorteio = self.sortear()


            print("===========================")
            print(figlet_format(sorteio, font="standard"))
            print("===========================")


            if len(sorteio) <= 3:
                self.falar(f"{sorteio[0]} {sorteio[1:]}")
            else:
                self.falar(sorteio)


            print("\n--- Pedras já sorteadas ---")
            print(sorted(list(self.numeros_sorteados)))


            if "FIM DE JOGO" in sorteio:
                break


            print("\nPróximo sorteio em 10 segundos...")
            time.sleep(10)


    def falar(self, texto):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(texto)
        engine.runAndWait()


bingo = Bingo()
bingo.jogar()