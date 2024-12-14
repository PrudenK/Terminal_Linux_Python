import os


def cat(op, directorioActual):
    if op == "cat":
        print("cat: falta un archivo")
    else:
        cat = op.split(" ")
        if len(cat) == 2:
            archivo = os.getcwd() + directorioActual + "/" + cat[1]
            if os.path.isdir(archivo):
                print(f"cat: {cat[1]} es un directorio")
            elif not os.path.exists(archivo):
                print(f"cat: '{cat[1]}' no existe")
            else:
                with open(archivo, "r", encoding="utf-8") as file:
                    for l in file.readlines():
                        print(l.strip())
        else:
            print("cat : solo acepta 1 archivo")