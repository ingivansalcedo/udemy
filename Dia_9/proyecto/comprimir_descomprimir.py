import shutil

carpeta_origen = 'E:\\Documents\\Cursos\\Udemy\\Python\\dia9\\proyecto'

archivo_destino = 'descubrir_proyecto'

# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Proyecto+Dia+9.zip', 'descubrir_proyecto', 'zip')