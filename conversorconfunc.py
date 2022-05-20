menu = """
Bienvenido al conversor de monedas.
Por favor, ingrese una opcion:
1 Con mis Pesos Colobianos, quiero saber cuantos dolares poseo. 
2 Con mis Pesos argentinos, quiero saber cuantos dolares poseo.
3 Con mis Pesos mexicanos, quiero saber cuantos dolares poseo.

"""
def conversor(tipo_pesos, dolar):
    pesos = input("Dime, Cuantos pesos " + tipo_pesos + " tienes? ")
    pesos = float(pesos) # Convierte a decimal
    valor_dolares = pesos / dolar
    valor_dolares = round(valor_dolares, 2) # Convierte con 2 decimales.
    valor_dolares = str(valor_dolares)
    print("Esto es lo que posees en dolares, U$D " + valor_dolares)

opcion = input(menu)

if opcion == "1":
    conversor("colombianos", 3875)
elif opcion == "2":
    conversor("argentinos", 180)
elif opcion == "3":
    conversor("mexicanos", 24)
else:
    print("La opcion no es correcta, ingrese nuevamente por favor.")    
