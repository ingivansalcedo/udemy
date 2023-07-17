import bs4
import requests

'''Obtiene y consulta información de una página, el esqueleto'''
resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

#print(resultado.text)

''' La función lxml lo convierte en un formato más legible'''
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

'''Ejemplo de como extraer informacion: Como ejemplo se utiliza la etiqueta <p></p>'''
# for i in range(len(sopa.select('p'))):
#     parrafoEspecial = sopa.select('p')[i].getText() #Obtiene solo el texto sin la configuración de la etiqueta
#     print(parrafoEspecial)

#header-image-wrapper
claseEspecial = sopa.select('.post-body.entry-content.float-container p')
for i in claseEspecial:
    print(i.getText())



