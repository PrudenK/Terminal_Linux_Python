import os
import subprocess


def nano(op, directorioActual):
    if op == "nano":
        print("nano: falta un archivo")
    else:
        nano = op.split(" ")
        if len(nano) == 2:
            subprocess.run(["konsole", "-e", "nano", os.getcwd() + directorioActual + "/" + nano[1]])
        else:
            print("nano : solo acepta 1 archivo")