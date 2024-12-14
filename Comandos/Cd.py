import os


def cd(op, directorioActual, directorioRaiz):
    cd = op.split(" ")
    if len(cd) > 2:
        print("cd: demasiados argumentos")
    elif len(cd) == 2:
        argumento = cd[1]
        if argumento == "..":
            if directorioActual != directorioRaiz:
                nuevoDirectorio = os.path.dirname(directorioActual)
                if os.path.commonpath([nuevoDirectorio, directorioRaiz]) == directorioRaiz:
                    return nuevoDirectorio
                else:
                    print("cd: no se puede salir del directorio del proyecto")
            else:
                print("cd: no se puede salir del directorio del proyecto")
        else:
            if argumento.startswith("/"):
                argumento = argumento[1:]

            nuevoDirectorio = os.getcwd() + os.path.abspath(os.path.join(directorioActual, argumento))

            if os.path.isdir(nuevoDirectorio):
                return nuevoDirectorio.replace(os.getcwd(), "")
            else:
                print(f"cd: {argumento}: No existe el archivo o el directorio")