# import zipfile

# mi_zip = zipfile.ZipFile('archivo_comprimido_python.zip','w')
#
# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')
#
# mi_zip.close()

# zip_abierto = zipfile.ZipFile('archivo_comprimido_python.zip','r')
# zip_abierto.extractall()

import shutil

carpeta_origen = 'E:\\Documents\\Cursos\\Udemy\\Python\\dia9\\comprimir_python'

archivo_destino = 'Todo_comprimido'

# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Todo_comprimido.zip', 'Extraccion Terminada', 'zip')