import os
from pathlib import Path
import shutil


# Imprimir el directorio actual
#print(Path(os.getcwd(), 'proyecto'))

# archivo = open('curso.txt', 'w')
# archivo.write('texto de prueba')
# archivo.close()
# print(os.listdir())

# shutil.move para mover archivos entre carpetas
#archivo_destino = Path(os.getcwd(), 'proyecto')
# shutil.move('curso.txt', archivo_destino)

# Eliminar archivos

# os.unlink(Path(archivo_destino, 'curso.txt'))

#Eliminar carpeta vacia
# os.rmdir()

#Eliminar todo
# shutil.rmtree()
carpeta_base = Path(os.getcwd())

archivo_busqueda = Path(carpeta_base, 'proyecto', 'descubrir_proyecto', 'Mi_Gran_Directorio')

#print(os.walk(archivo_busqueda))

# for carpeta, subcarpeta, archivo in os.walk(archivo_busqueda):
#     print(f'En la carpeta: {carpeta}')
#     print(f'Las subcarpetas son: ')
#     for sub in subcarpeta:
#         print(f'\t{sub}')
#     print('Los archivos son: ')
#     for arch in archivo:
#         print(f'\t{arch}')
#     print('\n')

for carpeta, subcarpeta, archivo in os.walk(archivo_busqueda):
    for arch in archivo:
        if arch.endswith('.txt'):
            print(f'\t{arch}')