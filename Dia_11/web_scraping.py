import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('title')[0].getText())
parrafoEspecial = sopa.select('p')
print(parrafoEspecial)


