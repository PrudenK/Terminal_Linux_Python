import os
import shutil


def cp(op, directorioActual):
    cp = op.split(" ")
    if op.startswith("cp -r"):

        if len(cp) < 4:
            print("cp -r: faltan argumentos")
        elif len(cp) == 4:
            archivo1 = os.getcwd() + directorioActual + "/" + cp[2]
            archivo2 = os.getcwd() + directorioActual + "/" + cp[3]
            if os.path.isdir(archivo1) and not os.path.isdir(archivo2):
                if not os.path.exists(archivo2):
                    shutil.copytree(archivo1, archivo2, dirs_exist_ok=True)
                else:
                    print(f"cp -r: no se puede sobreescribir el no directorio '{cp[3]}' con el directorio '{cp[2]}'")
            elif os.path.isdir(archivo1) and os.path.isdir(archivo2):
                shutil.copytree(archivo1, archivo2, dirs_exist_ok=True)
            else:
                shutil.copy(archivo1, archivo2)

    elif op == "cp":
        print("cp: faltan argumentos")
    else:
        if len(cp) == 3:
            try:
                archivo1 = os.getcwd() + directorioActual + "/" + cp[1]
                archivo2 = os.getcwd() + directorioActual + "/" + cp[2]
                if os.path.isdir(archivo1):
                    print("cp: -r no especificado para copiar un directorio")
                else:
                    shutil.copy(archivo1, archivo2)
            except Exception:
                print(f"cp: no existe el archivo '{cp[1]}'")
        else:
            print("cp: espera dos argumentos")