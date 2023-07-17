import time
import timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
prueba_for(100000)
fin = time.time()
duracion = fin - inicio
print(duracion)

inicio = time.time()
prueba_while(100000)
fin = time.time()
duracion = fin - inicio
print(duracion)

declaracion_for = '''
prueba_for(10)
'''
setup_for = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

declaracion_while = '''
prueba_while(10)
'''
setup_while = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion = timeit.timeit(declaracion_for, setup_for, number=1000000)
print(duracion)
duracion = timeit.timeit(declaracion_while, setup_while, number=1000000)
print(duracion)
