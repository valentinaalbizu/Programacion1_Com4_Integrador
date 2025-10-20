import csv

ARCHIVO_PAISES = "paises.csv"

# CARGA DE DATOS 

def cargar_paises(ruta_csv):
    """Carga los países desde un archivo CSV y valida los datos."""
    paises = []

    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    # Permitir diferentes formatos de encabezado
                    nombre = fila.get("nombre") or fila.get("Nombre")
                    poblacion = fila.get("poblacion") or fila.get("Población")
                    superficie = fila.get("superficie") or fila.get("Superficie_km2")
                    continente = fila.get("continente") or fila.get("Continente")

                    # Validar que todos los campos existan
                    if not (nombre and poblacion and superficie and continente):
                        raise ValueError("Faltan datos en la fila")

                    # Convertir tipos
                    pais = {
                        "nombre": nombre.strip(),
                        "poblacion": int(poblacion),
                        "superficie": int(superficie),
                        "continente": continente.strip()
                    }

                    paises.append(pais)

                except Exception:
                    print(f" Fila con formato incorrecto y se omitió: {fila}")

        if paises:
            print(f"\n Se cargaron correctamente {len(paises)} países.\n")
        else:
            print("\n No se cargó ningún país válido. Verificá el formato del CSV.\n")

    except FileNotFoundError:
        print("\n Error: No se encontró el archivo especificado.")
    except Exception as e:
        print(f"\n Error al leer el archivo: {e}")

    return paises


# FUNCIONES DE BÚSQUEDA Y FILTROS

def buscar_pais(paises, nombre):
    resultados = [p for p in paises if nombre.lower() in p["nombre"].lower()]
    if resultados:
        print(f"\n Se encontraron {len(resultados)} país(es) con el nombre '{nombre}':")
        mostrar_paises(resultados)
    else:
        print(f"\n No se encontró ningún país que contenga '{nombre}'.")


def filtrar_por_continente(paises, continente):
    resultados = [p for p in paises if p["continente"].lower() == continente.lower()]
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


# ORDENAMIENTOS 

def ordenar_paises(paises, campo, descendente=False):
    try:
        paises_ordenados = sorted(paises, key=lambda x: x[campo], reverse=descendente)
        print(f"\n Países ordenados por {campo} ({'descendente' if descendente else 'ascendente'}):")
        mostrar_paises(paises_ordenados)
    except KeyError:
        print(" Campo inválido para ordenar. Usá: nombre / poblacion / superficie.")


# ESTADÍSTICAS 

def mostrar_estadisticas(paises):
    if not paises:
        print(" No hay datos disponibles para mostrar estadísticas.")
        return

    pais_mayor = max(paises, key=lambda x: x["poblacion"])
    pais_menor = min(paises, key=lambda x: x["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)

    paises_por_continente = {}
    for p in paises:
        continente = p["continente"]
        paises_por_continente[continente] = paises_por_continente.get(continente, 0) + 1

    print("\n Estadísticas generales:")
    print(f"   ▫ País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']:,} hab.)")
    print(f"   ▫ País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']:,} hab.)")
    print(f"   ▫ Promedio de población: {int(promedio_poblacion):,} hab.")
    print(f"   ▫ Promedio de superficie: {int(promedio_superficie):,} km²")
    print("   ▫ Cantidad de países por continente:")
    for cont, cantidad in paises_por_continente.items():
        print(f"      - {cont}: {cantidad}")


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


# MENÚ PRINCIPAL 

def mostrar_menu():
    print("      MENÚ DE OPCIONES     ")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")


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
            print("\n Programa finalizado. ¡Hasta luego!")
            break

        else:
            print(" Opción inválida. Intentá de nuevo.")


# EJECUCIÓN 

if __name__ == "__main__":
    main()
