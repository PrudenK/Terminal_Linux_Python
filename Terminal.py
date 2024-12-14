import os
import subprocess
from datetime import datetime

from Comandos.Cat import cat
from Comandos.Cd import cd
from Comandos.Cp import cp
from Comandos.Firefox import firefox
from Comandos.Head import head
from Comandos.Mkdir import mkdir
from Comandos.Mv import mv
from Comandos.Nano import nano
from Comandos.Rm import rm
from Comandos.Tail import tail
from Comandos.Touch import touch
from Comandos.ls import ls

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
        directorioActual = cd(op, directorioActual, directorioRaiz) or directorioActual
    elif op == "pwd":
        print(directorioActual)
    elif op.startswith("mkdir"):
        mkdir(op, directorioActual)
    elif op.startswith("ls"):
        ls(op, directorioActual)
    elif op.startswith("touch"):
       touch(op, directorioActual)
    elif op.startswith("nano"):
        nano(op, directorioActual)
    elif op.startswith("cat"):
       cat(op, directorioActual)
    elif op.startswith("rm"):
        rm(op, directorioActual)
    elif op.startswith("echo "):
        texto = op.split("echo ")
        print(texto[1])

    elif op.startswith("cp"):
        cp(op, directorioActual)
    elif op.startswith("mv"):
        mv(op, directorioActual)
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
        firefox(op)
    elif op.startswith("grep"):
        pass
    elif op.startswith("head"):
        head(op, directorioActual)
    elif op.startswith("tail"):
        tail(op, directorioActual)
    elif op == "df":
        os.system("df")
    elif op == "exit":
        break
    else:
        print(f"{op}: comando no encontrado")