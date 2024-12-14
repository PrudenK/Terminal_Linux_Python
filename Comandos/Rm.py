import os
import shutil


def rm(op, directorioActual):
    if op == "rm" or op == "rm -r":
        print("rm: falta un openrado")
    else:
        if op.startswith("rm -r "):
            rm = op.split(" ")
            for file in rm[2:]:
                try:
                    path = os.getcwd() + directorioActual + "/" + file
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                except Exception:
                    print(f"rm: no se puede borrar '{file}': No existe el archivo")
        elif op.startswith("rm "):
            rm = op.split(" ")
            for file in rm[1:]:
                try:
                    path = os.getcwd() + directorioActual + "/" + file
                    if os.path.isdir(path):
                        print(f"rm: no sepuede borrar '{file}': Es un directorio")
                    else:
                        os.remove(path)
                except Exception:
                    print(f"rm: no se puede borrar '{file}': No existe el archivo")
        else:
            print("comando no encontrado")