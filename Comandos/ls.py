import os

RESET = "\033[0m"
BLUE = "\033[34m"
BOLD = "\033[1m"
YELLOW = "\033[33m"


def formato_ls(contenido, directorioActual):
    max_len = max(len(item) for item in contenido)
    columnas = 4
    filas = len(contenido) // columnas + (1 if len(contenido) % columnas > 0 else 0)

    for i in range(filas):
        row = []
        for j in range(i, len(contenido), filas):
            item = contenido[j]
            item_path = os.getcwd()+directorioActual+ "/"+ item
            if os.path.isdir(item_path):
                row.append(f"{BOLD}{BLUE}{item:<{max_len}}{RESET}")
            else:
                row.append(f"{item:<{max_len}}{RESET}")
        print("  ".join(row))

def lsParaMasArchivos(op, directorioActual, lsLen):
    listados = op.split(" ")
    if len(listados) > lsLen+1:
        for l in listados[lsLen:]:
            file = os.getcwd() + directorioActual + "/" + l

            if os.path.isdir(file):

                if lsLen == 1:
                    listado = [l for l in os.listdir(file) if not l.startswith(".")]
                else:
                    listado = os.listdir(file)

                print(f"{BOLD}{YELLOW}{l}{RESET}:")
                formato_ls(listado, directorioActual+ "/" + l)
            else:
                if os.path.exists(file):
                    print(f"{BOLD}{YELLOW}{l}{RESET} (no es un directorio):\n{l}")
                else:
                    print(f"'{l}' no existe")
    else:
        try:
            listado = os.listdir(os.getcwd() + directorioActual + "/" + listados[lsLen])
            if lsLen == 1:
                listado = [l for l in listado if not l.startswith(".")]

            formato_ls(listado, directorioActual+ "/" + listados[lsLen])
        except Exception:
            print(listados[lsLen])

