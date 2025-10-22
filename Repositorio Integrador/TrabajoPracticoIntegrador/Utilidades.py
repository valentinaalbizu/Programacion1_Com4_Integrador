# UTILIDADES 

# Muestra los países con todos sus datos de forma prolija
def mostrar_paises(lista_paises):
    for p in lista_paises:
        print(f"{p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")

# Pide al usuario un rango de valores (mínimo y máximo) para filtrar países
def pedir_rango(nombre_campo):
    try:
        minimo = int(input(f"Ingresá {nombre_campo} mínimo: "))
        maximo = int(input(f"Ingresá {nombre_campo} máximo: "))
        return minimo, maximo
    except ValueError:
        print("Entrada inválida. Debés ingresar números.")
        return None, 
import unicodedata

# Convierte texto a minúsculas, elimina espacios y acentos
def normalizar(texto):
    """Convierte texto a minúsculas, elimina espacios y acentos."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto