#tuplas
mi_tupla = (2,4)
print("mi tuple",mi_tupla)

#lista
mi_lista = [1,3,3.1416,"christian",mi_tupla]
print("el primer elemento de mi lista :",mi_lista[0])
print("el cuarto elemento de mi lista :",mi_lista[3])
print("el tercer elemento de mi lista :",mi_lista[2])

#diccionario 
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre": "chrintian",
    "pi":3.1416,
    "tel": "664-2334455"
}

print("llave para acceder a mi diccionario mi_lista",mi_diccionario["mi_lista"])
print("llave para acceder a pi",mi_diccionario["pi"])
print("llave para acceder a tel",mi_diccionario["tel"])

