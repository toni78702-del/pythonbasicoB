# el siguiente codigo hereda los metodos de enemigo para la clase de zombie:
from enemigo import *
import random

class zombie(enemigo):
    def __init__(self, puntos_energia=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("* Hummm...... *")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando de propagar la enfermedad!!")

    def ataque_especial(self):
        print("Zombie ataque especial")
        funciona_ataque_especial = random.random() < 0.50
        if funciona_ataque_especial:
            self.ataque += 2
            print('Zombie ha regenerado su energía con 2HP!!!')
