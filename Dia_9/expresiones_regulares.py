import re
import os
from pathlib import Path
import shutil

# texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
#
# patron = "ayuda"
#
# busqueda = re.search(patron, texto)
# print(busqueda)
#
# busqueda = re.findall(patron, texto)
# print(busqueda)
#
# for hallazgo in re.finditer(patron, texto):
#     print(hallazgo.span())

# ingivansalcedo@yahoo.com.co
# def verificar_email(email):
#     patron = r'^\D{1}\w+@[\w]+\.[\w]+\.?\w*$'
#     verificar = re.match(patron, email)
#     if verificar:
#         print("Ok")
#     else:
#         print("La dirección de email es incorrecta")
#
#
# email = input("Ingrese su email: ")
# verificar_email(email)


# def verificar_saludo(frase):
#     patron = r'^[H|h]ola{1}'
#     verificar = re.match(patron, frase)
#     if verificar:
#         print("Ok")
#     else:
#         print("No has saludado")
#
# verificar_saludo("Hola, este es un ejemplo")
# verificar_saludo("Este es un ejemplo, hola")
# verificar_saludo("Hagame caso")

# def verificar_cp(cp):
#     patron = r'^\w{2,2}\d{4,4}$'
#     verificar = re.match(patron, cp)
#     if verificar:
#         print("Ok")
#     else:
#         print("El código postal ingresado no es correcto")
#
# verificar_cp("XX1234")
# verificar_cp("4X123")
# verificar_cp("DF09876")

ruta_base = os.getcwd()
ruta_archivo = Path(ruta_base, 'archivo9.txt')
patron = r'N\w{3,3}-\d{5,5}'

archivo = ruta_archivo.open('r')
# print(archivo.read())
verificar = re.findall(patron, archivo.read())
print(type(verificar))
archivo.close()

#archivo2 = 'Fusce at ornare sapien. Curabitur vestibulum nibh in neque tincidunt, non interdum ante semper. Vivamus eget scelerisque eros. Vestibulum egestas elementum congue. Ut hendrerit ultrices nunc, quis elementum arcu. Fusce ullamcorper quam accumsan, commodo augue ac, viverra ipsum. Nlkj-41523 Pellentesque venenatis vehicula felis id placerat. Praesent mollis lobortis lorem, vel efficitur risus mollis eget. Quisque molestie sapien quis enim ultrices mollis nec eu lacus.'
#existe = re.findall(patron, archivo2)
#print(existe)


