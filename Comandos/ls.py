def formato_ls(contenido):
    max_len = max(len(item) for item in contenido)
    columnas = 4
    filas = len(contenido) // columnas + (1 if len(contenido) % columnas > 0 else 0)

    for i in range(filas):
        row = [contenido[j] for j in range(i, len(contenido), filas)]
        print("".join(f"{item:<{max_len}}  " for item in row))