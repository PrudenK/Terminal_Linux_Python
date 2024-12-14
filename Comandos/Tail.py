import os


def tail(op, directorioActual):
    tail = op.split(" ")
    if op.startswith("tail -n"):
        if len(tail) == 4:
            file = os.getcwd() + directorioActual + "/" + tail[3]
            if os.path.exists(file):
                if os.path.isdir(file):
                    print("tail -n: no funciona con directorios")
                else:
                    continuar = True
                    try:
                        numLineas = int(tail[2])
                    except Exception:
                        continuar = False
                        print("tail -n: solo acepta parametros enteros")

                    if continuar:
                        with open(file, "r", encoding="utf-8") as archivo:
                            lineas = archivo.readlines()

                            for line in lineas[-numLineas:]:
                                print(line.strip())
            else:
                print(f"tail: '{tail[3]}' no existe")
        else:
            print("tail -n: número incorrecto de argumentos")
    elif op.startswith("tail "):
        if len(tail) == 2:
            file = os.getcwd() + directorioActual + "/" + tail[1]

            if os.path.exists(file):
                if os.path.isdir(file):
                    print("tail: no funciona con directorios")
                else:
                    with open(file, "r", encoding="utf-8") as archivo:
                        lineas = archivo.readlines()

                        for line in lineas[-10:]:
                            print(line.strip())
            else:
                print(f"tail: '{tail[1]}' no existe")
        else:
            print("tail: número incorrecto de argumentos")