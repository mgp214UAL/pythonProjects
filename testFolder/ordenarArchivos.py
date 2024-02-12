import os

nueva_carpeta = "files"

if not os.path.exists(nueva_carpeta):
    os.makedirs(nueva_carpeta)

with os.scandir(os.getcwd()) as ls:
    for entrada in ls: 
        if entrada.is_file():
            os.rename(entrada.path, os.path.join(nueva_carpeta, entrada.name))
