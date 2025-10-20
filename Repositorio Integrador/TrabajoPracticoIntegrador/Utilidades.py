# UTILIDADES 

def mostrar_paises(lista_paises):
    for p in lista_paises:
        print(f"   {p['nombre']} | Población: {p['poblacion']:,} | Superficie: {p['superficie']:,} km² | Continente: {p['continente']}")


def pedir_rango(nombre_campo):
    try:
        minimo = int(input(f"Ingresá {nombre_campo} mínimo: "))
        maximo = int(input(f"Ingresá {nombre_campo} máximo: "))
        return minimo, maximo
    except ValueError:
        print(" Entrada inválida. Debés ingresar números.")
        return None, None