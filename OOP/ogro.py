
from enemigo import *
import random

class ogro(enemigo):
    def __init__(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Ahhhhhh!! Aplasta todo!!!!")

    def ataque_especial(self):
        print("Ogro ataque especial")
        funciona_ataque_especial = random.random() < 0.20
        if self.ataque_especial:
            self.ataque += 4
            print('Ogro enojado e incremento su ataque por 4!!!')