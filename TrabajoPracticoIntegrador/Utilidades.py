"""
Funciones auxiliares para mostrar países, pedir rangos y normalizar texto.
"""

import unicodedata

def mostrar_paises(lista_paises):
    """Muestra los países con todos sus datos de forma prolija."""
    
    for p in lista_paises:
        print(f"{p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")

def pedir_rango(nombre_campo):
    """Pide al usuario un rango de valores (mínimo y máximo) para filtrar países."""

    try:
        minimo = int(input(f"Ingresá {nombre_campo} mínimo: "))
        maximo = int(input(f"Ingresá {nombre_campo} máximo: "))
        return minimo, maximo
    except ValueError:
        print("Entrada inválida. Debés ingresar números.")
        return None, None 

def normalizar(texto):
    """Convierte texto a minúsculas, elimina espacios y acentos."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto
