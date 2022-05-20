import random

def generar_contra():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros # suma todas las listas y crea una sola combinada

    contraseña = [] #Se crea una lista vacia

    for i in range(15):
        caracter_random = random.choice(caracteres) #caracteres aleatorios
        contraseña.append(caracter_random) #agrego caracteres a la lista

    contraseña = "".join(contraseña) #uno los elementos de la lista
    return contraseña


def run():
    contraseña = generar_contra()
    print("La nueva contraseña es: " + contraseña) 


if __name__ == "__main__":
    run()