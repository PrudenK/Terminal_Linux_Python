import os


def head(op, directorioActual):
    head = op.split(" ")
    if op.startswith("head -n"):
        if len(head) == 4:
            file = os.getcwd() + directorioActual + "/" + head[3]
            if os.path.exists(file):
                if os.path.isdir(file):
                    print("head -n: no funciona con directorios")
                else:
                    continuar = True
                    try:
                        numLineas = int(head[2])
                    except Exception:
                        continuar = False
                        print("head -n: solo acepta parametros enteros")

                    if continuar:
                        archivo = open(file, "r", encoding="utf-8")

                        for _ in range(numLineas):
                            linea = archivo.readline().strip()
                            if not linea:
                                break
                            print(linea)

                        archivo.close()
            else:
                print(f"head: '{head[3]}' no existe")
        else:
            print("head -n: número incorrecto de argumentos")
    elif op.startswith("head "):
        if len(head) == 2:
            file = os.getcwd() + directorioActual + "/" + head[1]

            if os.path.exists(file):
                if os.path.isdir(file):
                    print("head: no funciona con directorios")
                else:
                    archivo = open(file, "r", encoding="utf-8")

                    for _ in range(10):
                        linea = archivo.readline().strip()
                        if not linea:
                            break
                        print(linea)

                    archivo.close()
            else:
                print(f"head: '{head[1]}' no existe")
        else:
            print("head: número incorrecto de argumentos")