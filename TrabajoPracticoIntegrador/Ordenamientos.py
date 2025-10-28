"""
Funciones para ordenar países por nombre, población o superficie.
"""

from Funciones import *

def ordenar_paises(paises, campo, descendente=False):
    """Ordena los países según el campo elegido (nombre, población o superficie)."""
    try:
        campo_norm = normalizar(campo)

        # Coincidencias parciales para facilitar entrada del usuario
        if "nom" in campo_norm:
            campo = "nombre"
        elif "pob" in campo_norm:
            campo = "poblacion"
        elif "sup" in campo_norm:
            campo = "superficie"

        # Ordenamiento alfabético
        if campo == "nombre":
            paises_ordenados = sorted(paises, key=lambda x: normalizar(x["nombre"]), reverse=descendente)

        # Ordenamiento numérico
        elif campo in ["poblacion", "superficie"]:
            paises_ordenados = sorted(paises, key=lambda x: x[campo], reverse=descendente)
        else:
            print("Campo inválido para ordenar. Usá: nombre / poblacion / superficie.")
            return

        print(f"\nPaíses ordenados por {campo} ({'descendente' if descendente else 'ascendente'}):")
        mostrar_paises(paises_ordenados)

    except Exception as e:
        print(f"Error al ordenar: {e}")

