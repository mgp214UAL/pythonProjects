import os
import time

def buscar_archivo(archivo, ruta="C:/"):
    archivos = 0
    
    rutas_encontradas = []

    for root, dirs, files in os.walk(ruta):
        for file_name in files:
            archivos += 1
            if file_name == archivo:
                # Si se encuentra el archivo, agregar la ruta a la lista
                rutas_encontradas.append((file_name, os.path.join(root, file_name)))

    return rutas_encontradas, archivos
archivo = input("Dime el archivo exacto que quieres que te diga su ruta: ")


inicio = time.time()

rutas, cantidad_archivos = buscar_archivo(archivo)

fin = time.time()

tiempo_total = fin - inicio

for nombre_archivo, ruta in rutas:
    print(f"El archivo '{nombre_archivo}' se encuentra en la ruta: {ruta}")
print(f"Se encontraron en total {len(rutas)} archivos con el nombre '{archivo}'.")
   

print(f"La búsqueda tomó {tiempo_total} segundos.")
print(f"Se iteraron {cantidad_archivos} archivos en total.")
