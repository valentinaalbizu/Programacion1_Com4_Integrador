import csv 
import unicodedata 

from Funciones import *
from Estadisticas import *
from CargaDeDatos import *
from Ordenamientos import *
from Utilidades import *

ARCHIVO_PAISES = "paises.csv"

# MENÚ PRINCIPAL 

def mostrar_menu():
    print("      MENÚ DE OPCIONES     ")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Agregar un país")
    print("8. Editar población y superficie de un país")
    print("9. Salir")


def main():
    paises = cargar_paises(ARCHIVO_PAISES)

    if not paises:
        print(" No se pudo cargar ningún país. Cerrando programa.")
        return

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Ingresá el nombre (o parte del nombre) del país: ")
            buscar_pais(paises, nombre)

        elif opcion == "2":
            continente = input("Ingresá el nombre del continente: ")
            filtrar_por_continente(paises, continente)

        elif opcion == "3":
            min_pob, max_pob = pedir_rango("población")
            if min_pob is not None:
                filtrar_por_rango(paises, "poblacion", min_pob, max_pob)

        elif opcion == "4":
            min_sup, max_sup = pedir_rango("superficie")
            if min_sup is not None:
                filtrar_por_rango(paises, "superficie", min_sup, max_sup)

        elif opcion == "5":
            campo = input("Campo para ordenar (nombre/poblacion/superficie): ").lower()
            descendente = input("¿Querés orden descendente? (s/n): ").lower() == "s"
            ordenar_paises(paises, campo, descendente)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            agregar_pais(paises)

        elif opcion == "8":
            editar_pais(paises)

        elif opcion == "9":
            print("\n Programa finalizado. ¡Hasta luego!")
            break

        else:
            print(" Opción inválida. Intentá de nuevo.")


# EJECUCIÓN 

if __name__ == "__main__":
    main()
