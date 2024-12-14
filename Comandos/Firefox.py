import subprocess


def firefox(op):
    if len(op.split(" ")) == 2:
        subprocess.Popen(["firefox", op.split(" ")[1]])
    elif len(op.split(" ")) > 2:
        print("firefox: demasiados argumentos")
    else:
        subprocess.Popen(["firefox"])