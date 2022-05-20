def palindromo(palabra):
    palabra = palabra.replace(" ", "")  #saco los espacios
    palabra = palabra.lower() #todo a minuscula
    palabra_inv = palabra[::-1]
    if palabra == palabra_inv:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("La palabra es palindromo")
    else:
        print("La palabra no es palindromo")


if __name__ == "__main__":
    run()
