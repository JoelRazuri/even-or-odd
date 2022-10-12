"""
    Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

    Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje
    con el resultado.

    Ejemplo:

    Mensaje que se muestra: ¿En qué número estás pensando?
    Entrada: 25
    Salida: ¡Es un número impar! ¿Puedes añadir otro?
"""


import os


def validar_numero(numero):

    if (numero>=1 and numero<=1000):
        continuar = True
    else:
        continuar = False

    return continuar


def es_par_o_impar(numero):

    if numero%2==0:
        print("Salida: El número es par.")
    else:
        print("Salida: El número es impar.")

def main():
    
    continuar = False
    
    while not continuar:
        os.system("cls")
        print("PAR O IMPAR")
        print("-"*10)
        numero = int(input("Elija un número entre 1 y 1000:"))
        continuar = validar_numero(numero)
        if not continuar:
            input("El número no es válido. Tiene que estar entre 1 y 1000...")

    print(f"Entrada: {numero}")
    es_par_o_impar(numero)
    print()
    respuesta = input("Desea ingresar otro número? (si/no):")
    # validar_respuesta(respuesta)
    if respuesta=='si':
        main()
    else:
        print("Hasta luego!!!")

if __name__ == "__main__":
    main()