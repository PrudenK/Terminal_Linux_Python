import os


def mkdir(op, directorioActual):
    mkdir = op.split(" ")
    if len(mkdir) == 1:
        if op == "mkdir":
            print("mkdir: falta un operando")
        else:
            print(f"Orden <<{op}>> no encontrada")
    else:
        for directorio in mkdir[1:]:
            try:
                os.mkdir(os.path.join(os.getcwd() + directorioActual, directorio))
            except FileExistsError:
                print(f"mkdir: no se puede crear el directorio <<{directorio}>>: El archivo ya existe")