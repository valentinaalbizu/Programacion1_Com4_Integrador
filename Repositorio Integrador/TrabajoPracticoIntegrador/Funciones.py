# FUNCIONES DE BÚSQUEDA, FILTROS, NORMALIZAR TEXTO, EDITAR Y AGREGAR PAISES
import unicodedata 
from Utilidades import *

def normalizar(texto):
    """Convierte texto a minúsculas, elimina espacios y acentos."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

def buscar_pais(paises, nombre):
    nombre_normalizado = normalizar(nombre)
    resultados = [p for p in paises if nombre_normalizado in normalizar(p["nombre"])]
    if resultados:
        print(f"\n Se encontraron {len(resultados)} país(es) con el nombre '{nombre}':")
        mostrar_paises(resultados)
    else:
        print(f"\n No se encontró ningún país que contenga '{nombre}'.")


def filtrar_por_continente(paises, continente):
    continente_normalizado = normalizar(continente)
    resultados = [p for p in paises if continente_normalizado in normalizar(p["continente"])]
    if resultados:
        print(f"\n Países en el continente '{continente}':")
        mostrar_paises(resultados)
    else:
        print(f"\n No se encontraron países en el continente '{continente}'.")


def filtrar_por_rango(paises, campo, minimo, maximo):
    resultados = [p for p in paises if minimo <= p[campo] <= maximo]
    if resultados:
        print(f"\n Países con {campo} entre {minimo} y {maximo}:")
        mostrar_paises(resultados)
    else:
        print(f"\n No hay países con {campo} en ese rango.")


def editar_pais(paises):
    print("\n Editar país ")
    nombre = input("Ingresá el nombre del país que querés editar: ")
    nombre_normalizado = normalizar(nombre)

    resultados = [p for p in paises if nombre_normalizado in normalizar(p["nombre"])]

    if not resultados:
        print(f" No se encontró ningún país que contenga '{nombre}'.")
        return

    print(f"\nSe encontraron {len(resultados)} país(es):")
    for i, p in enumerate(resultados):
        print(f"{i + 1}. {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km²")

    try:
        indice = int(input("Elegí el número del país que querés editar: ")) - 1
        if indice < 0 or indice >= len(resultados):
            print(" Número inválido.")
            return

        pais = resultados[indice]
        nueva_poblacion = int(input(f"Nueva población para {pais['nombre']}: "))
        nueva_superficie = float(input(f"Nueva superficie para {pais['nombre']} (km²): "))

        pais["poblacion"] = nueva_poblacion
        pais["superficie"] = nueva_superficie

        print(f"Datos actualizados para {pais['nombre']}.")

    except ValueError:
        print("Entrada inválida.")

def agregar_pais(paises):
    print("\n--- Agregar nuevo país ---")
    nombre = input("Nombre del país: ").strip()
    continente = input("Continente: ").strip()

    try:
        poblacion = int(input("Población: "))
        superficie = float(input("Superficie (km²): "))
    except ValueError:
        print("Error: Población y superficie deben ser numéricos.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print(f"País '{nombre}' agregado correctamente.")

