"""
Programa principal de gestión de países.
Permite buscar, filtrar, ordenar, editar y agregar países desde un archivo CSV.
Incluye validaciones, estadísticas y persistencia de datos.
"""

import csv
import os
import unicodedata

# Importación de módulos propios
from Funciones import *
from Estadisticas import *
from CargaDeDatos import *
from Ordenamientos import *
from Utilidades import *

ARCHIVO_PAISES = "paises.csv"

# Verifica si el archivo existe; si no, lo crea con encabezados
if not os.path.exists(ARCHIVO_PAISES):
    with open(ARCHIVO_PAISES, "w", newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
    print(f"Archivo '{ARCHIVO_PAISES}' creado automáticamente.")

# Muestra el menú principal de opciones
def mostrar_menu():
    print("\n     - MENÚ DE OPCIONES -     ")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Agregar un país")
    print("8. Editar población y superficie de un país")
    print("9. Guardar cambios en el archivo CSV")
    print("10. Salir")

# Guarda los datos actualizados en el archivo CSV
def guardar_paises(paises, ruta_csv):
    try:
        with open(ruta_csv, "w", newline='', encoding='utf-8') as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        print(f"\nCambios guardados correctamente en '{ruta_csv}'.")
    except Exception as e:
        print(f"\nError al guardar el archivo: {e}")

# Función principal del programa
def main():
    paises = cargar_paises(ARCHIVO_PAISES)

    if not paises:
        print(" No se cargó ningún país. Podés agregar países desde el menú.")

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if not opcion.isdigit():
            print("Entrada inválida. Debés ingresar un número.")
            continue

        # Opción 1: buscar país
        if opcion == "1":
            nombre = input("Ingresá el nombre (o parte del nombre) del país: ")
            buscar_pais(paises, nombre)

        # Opción 2: filtrar por continente
        elif opcion == "2":
            continente = input("Ingresá el nombre del continente: ")
            filtrar_por_continente(paises, continente)

        # Opción 3: filtrar por rango de población
        elif opcion == "3":
            min_pob, max_pob = pedir_rango("población")
            if min_pob is not None:
                filtrar_por_rango(paises, "poblacion", min_pob, max_pob)

        # Opción 4: filtrar por rango de superficie
        elif opcion == "4":
            min_sup, max_sup = pedir_rango("superficie")
            if min_sup is not None:
                filtrar_por_rango(paises, "superficie", min_sup, max_sup)

        # Opción 5: ordenar países
        elif opcion == "5":
            campo = input("Campo para ordenar (nombre/poblacion/superficie): ").lower()
            descendente = input("¿Querés orden descendente? (s/n): ").lower() == "s"
            ordenar_paises(paises, campo, descendente)

        # Opción 6: mostrar estadísticas
        elif opcion == "6":
            mostrar_estadisticas(paises)

        # Opción 7: agregar país
        elif opcion == "7":
            agregar_pais(paises)

        # Opción 8: editar país
        elif opcion == "8":
            editar_pais(paises)

        # Opción 9: guardar cambios
        elif opcion == "9":
            guardar_paises(paises, ARCHIVO_PAISES)

        # Opción 10: salir
        elif opcion == "10":
            print("\nPrograma finalizado. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")

# Punto de entrada
if __name__ == "__main__":
    main()