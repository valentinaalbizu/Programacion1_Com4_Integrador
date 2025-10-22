#Carga De Datos
import csv

def cargar_paises(ruta_csv):
    """Carga los países desde un archivo CSV y valida los datos."""
    paises = []

    try:
        # Acá abrimos el archivo CSV para leer los países y recorrer cada fila

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
                        "superficie": float(superficie),
                        "continente": continente.strip()
                    }
                    
                    paises.append(pais)

                except Exception:
                    print(f"Fila con formato incorrecto y se omitió: {fila}")

        if paises:
            print(f"\nSe cargaron correctamente {len(paises)} países.\n")
        else:
            print("\nNo se cargó ningún país válido. Verificá el formato del CSV.\n")

    except FileNotFoundError:
        print("\nError: No se encontró el archivo especificado.")
    except Exception as e:
        print(f"\nError al leer el archivo: {e}")
        
    # Devuelve la lista final de países ya cargados

    return paises
