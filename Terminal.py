import os
import shutil
import subprocess
from datetime import datetime
from Comandos.ls import formato_ls, lsParaMasArchivos

RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[36m"
BOLD = "\033[1m"
YELLOW = "\033[33m"

directorioRaiz = "/Terminal"
directorioActual = os.path.join(directorioRaiz, "home/pruden")

while True:
    prompt = f"{BOLD}{CYAN}pruden@Terminal:{RESET}{GREEN}{directorioActual}{RESET}$ "
    op = input(prompt).strip()
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
        if op.startswith("ls -a "):
            lsParaMasArchivos(op, directorioActual, 2)
        elif op.startswith("ls ") and not op.startswith("ls -a"):
            lsParaMasArchivos(op, directorioActual, 1)
        elif op == "ls":
            listado = os.listdir(os.getcwd()+ directorioActual)
            formato_ls([l for l in listado if not l.startswith(".")], directorioActual)
        elif op == "ls -a":
            listado = os.listdir(os.getcwd() + directorioActual)
            formato_ls(listado, directorioActual)

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
                archivo = os.getcwd()+directorioActual+"/"+cat[1]
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
                    archivo1 = os.getcwd()+directorioActual+"/"+cp[1]
                    archivo2 = os.getcwd()+directorioActual+"/"+cp[2]
                    if os.path.isdir(archivo1):
                        print("cp: -r no especificado para copiar un directorio")
                    else:
                        shutil.copy(archivo1, archivo2)
                except Exception:
                    print(f"cp: no existe el archivo '{cp[1]}'")
            else:
                print("cp: espera dos argumentos")

    elif op.startswith("mv"):
        if op == "cp":
            print("mv: faltan argumentos")
        else:
            mv = op.split(" ")
            if len(mv) == 3:
                archivo1 = os.getcwd()+directorioActual+"/"+mv[1]
                archivo2 = os.getcwd()+directorioActual+"/"+mv[2]
                if os.path.isdir(archivo2):
                    shutil.move(archivo1, archivo2)
                else:
                    if os.path.isdir(archivo1):
                        print(f"mv: no se puede sobreescribir el no directorio {mv[2]} con el directorio {mv[1]}")
                    else:
                        os.rename(archivo1, archivo2)
    elif op == "ps -aux" or op == "ps aux":
        os.system("ps aux")
    elif op == "ps":
        os.system("ps")
    elif op == "ip addr":
        os.system("ip addr")
    elif op.startswith("man "):
        os.system(op)
    elif op == "top":
        result = subprocess.run(['ps', '-e', '-o', 'pid,comm'], capture_output=True, text=True)
        print(result.stdout)

    elif op == "clear":
        os.system("clear")
    elif op == "whoami":
        print(os.getlogin())
    elif op == "time":
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    elif op.startswith("firefox"):
        if len(op.split(" ")) == 2:
            subprocess.Popen(["firefox",op.split(" ")[1]])
        elif len(op.split(" ")) > 2:
            print("firefox: demasiados argumentos")
        else:
            subprocess.Popen(["firefox"])

    elif op.startswith("grep "):
        pass

    elif op.startswith("head"):
        if op.startswith("head -n"):
            head = op.split(" ")
            if os.path.exists(os.getcwd()+directorioActual+"/"+head[3]):
                continuar = True
                try:
                    numLineas = int(head[2])
                except Exception:
                    continuar = False
                    print("head: solo acepta parametros enteros")

                if continuar:
                    archivo = open(os.getcwd()+directorioActual+"/"+head[3], "r", encoding="utf-8")

                    for _ in range(numLineas):
                        print(archivo.readline().strip())

                    archivo.close()

    elif op == "df":
        os.system("df")
    elif op == "exit":
        break
    else:
        print(f"{op}: comando no encontrado")