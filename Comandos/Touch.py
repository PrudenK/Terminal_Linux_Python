import os


def touch(op, directorioActual):
    if op.startswith("touch "):
        touchVector = op.split(" ")

        try:
            for archivo in touchVector[1:]:
                file = open(os.getcwd() + directorioActual + "/" + archivo, "w", encoding="utf-8")
                file.close()
        except Exception:
            pass

    elif op == "touch":
        print("touch: falta un archivo como argumento")
    else:
        print(f"Orden <<{op}>> no encontrada")