import os
import shutil


def mv(op, directorioActual):
    if op == "mv":
        print("mv: faltan argumentos")
    else:
        mv = op.split(" ")
        if len(mv) == 3:
            archivo1 = os.getcwd() + directorioActual + "/" + mv[1]
            archivo2 = os.getcwd() + directorioActual + "/" + mv[2]
            if os.path.exists(archivo1):
                if os.path.isdir(archivo2):
                    shutil.move(archivo1, archivo2)
                else:
                    if os.path.isdir(archivo1):
                        print(f"mv: no se puede sobreescribir el no directorio {mv[2]} con el directorio {mv[1]}")
                    else:
                        os.rename(archivo1, archivo2)
            else:
                print(f"mv: '{mv[1]}' no existe")