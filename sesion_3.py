# loops 
mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("el numero es",i)

resultado = 0 
for i in mi_lista:
    resultado +=1 

print(f"el resultado de la suma de mi lista es: {resultado}")

for i in range (2,9):
    print(i)

mi_lista_2 = ["lunes","martes","miercoles","jueves","viernes"]
for i in mi_lista_2:
    if i != "lunes":
        print(f"feliz {i}!")

#whilw loop
i = 0

while i < 5:
    i += 1
    if i==3:
        continue
    print(i)
    if i==4:
        break
else:
    print("i e ahora mayor o igual a 5")

#practica 2 
#dada la lista_2 = ["lunes","martes","miercoles","jueves","viernes "]
#imprimir cada elemento de la lista_3 y cuando sea lunes no lo inclutas 
#pista:usa los dos tipos de loops while y for el mismo programa para lograrlo
#resultado 
#martes 
#miercoles 
#jueves 
#vieres
#martes 
#miercoles 
#jueves 
#vieres
#martes 
#miercoles 
#jueves 
#vieres


x = 0
while x < 3:
    x += 1
    for i in mi_lista_2:
        if i != "lunes":
            print(str(i))