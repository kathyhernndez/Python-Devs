def conversor(tipo_moneda, valor_dolar):
    bolivares = input("¿Cúantos " + tipo_moneda + "Tienes?: ")
    pesos = float(bolivares)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dólares")

menu = """
Bienvenido a Conversor de Monedas💲


1 - Bolivares Venezolanos 
2 - Pesos Argentino 
3 - Pesos Mexicanos 

Elige Una Opcion: 



"""
opcion = int(input(menu))



if opcion == 1:
    conversor("Bolivares", 4000)
elif opcion == 2:
    conversor("Pesos Argentinnos", 65)
elif opcion == 3:
    conversor("Pesos Mexicanos", 24)
else:
    print("Ingresa una opcion correcta por favor")



