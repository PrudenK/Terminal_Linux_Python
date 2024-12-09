import os
import shutil
import subprocess

from samba.dcerpc.security import privilege_name

from Comandos.ls import formato_ls

comandos = ["cd", "ls", "mkdir", "pwd"]

directorioRaiz = "/Terminal"
directorioActual = os.path.join(directorioRaiz, "home/pruden")

while True:
    op = input("pruden@Terminal:" + directorioActual + "$ ").strip()
    if op.startswith("cd"):
        cd = op.split(" ")
        if len(cd) > 2:
            print("cd: demasiados argumentos")
        elif len(cd) == 2:
            argumento = cd[1]
            if argumento == "..":
                if directorioActual != directorioRaiz:
                    nuevoDirectorio = os.path.dirname(directorioActual)
                    if os.path.commonpath([nuevoDirectorio, directorioRaiz]) == directorioRaiz:
                        directorioActual = nuevoDirectorio
                    else:
                        print("cd: no se puede salir del directorio del proyecto")
                else:
                    print("cd: no se puede salir del directorio del proyecto")
            else:
                if argumento.startswith("/"):
                    argumento = argumento[1:]

                nuevoDirectorio = os.getcwd() + os.path.abspath(os.path.join(directorioActual, argumento))

                if os.path.isdir(nuevoDirectorio):
                    directorioActual = nuevoDirectorio.replace(os.getcwd(), "")
                else:
                    print(f"cd: {argumento}: No existe el archivo o el directorio")



    elif op == "pwd":
        print(directorioActual)
    elif op.startswith("mkdir"):
        mkdir = op.split(" ")
        if len(mkdir) == 1:
            if op == "mkdir":
                print("mkdir: falta un operando")
            else:
                print(f"Orden <<{op}>> no encontrada")
        else:
            for directorio in mkdir[1:]:
                try:
                    os.mkdir(os.path.join(os.getcwd()+ directorioActual, directorio))
                except FileExistsError:
                    print(f"mkdir: no se puede crear el directorio <<{directorio}>>: El archivo ya existe")



    elif op.startswith("ls"):


        if op == "ls":
            listado = os.listdir(os.getcwd()+ directorioActual)
            formato_ls([l for l in listado if not l.startswith(".")])
        elif op == "ls -a":
            listado = os.listdir(os.getcwd() + directorioActual)
            formato_ls(listado)

    elif op.startswith("touch"):
        if op.startswith("touch "):
            touchVector = op.split(" ")

            try:
                for archivo in touchVector[1:]:
                    file = open(os.getcwd()+directorioActual+"/"+archivo, "w", encoding="utf-8")
                    file.close()
            except Exception:
                pass

        elif op == "touch":
            print("touch: falta un archivo como argumento")
        else:
            print(f"Orden <<{op}>> no encontrada")
    elif op.startswith("nano"):
        if op == "nano":
            print("nano: falta un archivo")
        else:
            nano = op.split(" ")
            if len(nano) == 2:
                subprocess.run(["konsole","-e", "nano", os.getcwd()+directorioActual+"/"+nano[1]])
            else:
                print("nano : solo acepta 1 archivo")

    elif op.startswith("cat"):
        if op == "cat":
            print("cat: falta un archivo")
        else:
            cat = op.split(" ")
            if len(cat) == 2:
                if os.path.isdir(os.getcwd()+directorioActual+"/"+cat[1]):
                    print(f"cat: {cat[1]} es un directorio")
                else:
                    with open(os.getcwd()+directorioActual+"/"+cat[1], "r", encoding="utf-8") as file:
                        for l in file.readlines():
                            print(l.strip())
            else:
                print("cat : solo acepta 1 archivo")
    elif op.startswith("rm"):
        if op == "rm" or op == "rm -r":
            print("rm: falta un openrado")
        else:
            if op.startswith("rm -r "):
                rm = op.split(" ")
                for file in rm[2:]:
                    try:
                        path = os.getcwd()+directorioActual+"/"+file
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
                        path = os.getcwd()+directorioActual+"/"+file
                        if os.path.isdir(path):
                            print(f"rm: no sepuede borrar '{file}': Es un directorio")
                        else:
                            os.remove(path)
                    except Exception:
                        print(f"rm: no se puede borrar '{file}': No existe el archivo")
            else:
                print("comando no encontrado")

    elif op.startswith("echo "):
        texto = op.split("echo ")
        print(texto[1])

    elif op.startswith("cp"):


        if op == "cp":
            print("cp: faltan argumentos")
        else:
            cp = op.split(" ")
            if len(cp) == 3:
                pass


    elif op == "clear":
        #os.system("clear")
        pass
    elif op == "exit":
        break
    else:
        print(f"{op}: comando no encontrado")


