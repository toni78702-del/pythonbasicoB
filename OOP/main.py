# Se hereda los metodos de las anteriores clases:
from enemigo import *
from zombie import *
from ogro import *

# Se registran los valores en variables para main:
Zombie = zombie(10, 1)
Ogro = ogro(20, 3)

def batalla(e1: enemigo, e2: enemigo):
    e1.habla()
    e2.habla()

    while e1.puntos_energia > 0 and e2.puntos_energia > 0:
        print("***************************")
        e1.ataque_especial()
        e2.ataque_especial()
        print(f"{e1.get_tipo_enemigo()}: quedan {e1.puntos_energia} puntos de energía !!!")
        print(f"{e2.get_tipo_enemigo()}: quedan {e2.puntos_energia} puntos de energía !!!")
        print(f"Ataque: {e2.ataque}")
        e1.puntos_energia -= e2.ataque
        print("///////////////////////////")
        print(f"Ataque: {e1.ataque}")
        e2.puntos_energia -= e1.ataque

    print("*******************************")
    if e1.puntos_energia > 0:
        print(f"{e1.get_tipo_enemigo()} gano !!!!")
    else:
        print(f"{e2.get_tipo_enemigo()} gano !!!!")

print(" ================ BATALLA ================ ")

batalla(Zombie, Ogro)

print(" ============== FIN DE LA BATALLA ============== ")


# Se usan los metodos de las clases y hace su correspondiente accion:
# print(f"{Zombie.get_tipo_enemigo()} tiene {Zombie.puntos_energia} de enegía y puede hacer {Zombie.ataque} de daño")
# print(f"{Zombie.habla()}")
# print(f"{Ogro.get_tipo_enemigo()} tiene {Ogro.puntos_energia} de enegía y puede hacer {Ogro.ataque} de daño")
# print(f"{Ogro.habla()}")