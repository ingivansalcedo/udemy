# from collections import Counter
#
# numeros = [8,6,9,5,6,7,7,7,7,4,5,6,5,5,4,3]
#
# print(Counter(numeros))
# print(Counter("mississippi"))
#
# frase = 'al pan pan y al vino vino'
# print(Counter(frase.split()))
#
# serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4])
# print(serie.most_common(2))

# from collections import defaultdict

# mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
#
# print(mi_dic['cuatro'])

# mi_dic2 = defaultdict(lambda: 'nada')
# mi_dic2['uno']= 'verde'
#
# print(mi_dic2['dos'])
# print(mi_dic2)

# from collections import namedtuple

# mi_tupla = (500,18, 65)
# print(mi_tupla[2])

# Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
# ariel = Persona('Ariel', 1.76, 79)

# print(ariel.nombre)
# print(ariel.altura)
# print(ariel.peso)
# print(ariel[2])

from collections import deque
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.appendleft("Bogota")
print(lista_ciudades)
