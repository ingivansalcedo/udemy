from datetime import datetime
hoy = datetime.now().date()
print(hoy)


# import  datetime
#
#
# mi_hora = datetime.time(17, 35, 50, 1500)
# print(type(mi_hora))  # <class 'datetime.time'>
# print(mi_hora)  # 17:35:50.001500
#
# mi_dia = datetime.date(2025, 10, 17)
# print(mi_dia)  # 2025-10-17
# print(mi_dia.year)  # 2025
# print(mi_dia.ctime())  # Fri Oct 17 00:00:00 202
#
# '''2023-09-17 Mientras la variable sea fecha, imprime fecha actual independiente
# de la información que tenga la variable'''
# print(mi_dia.today())
#
# from datetime import datetime
#
# mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
# print(mi_fecha)  # 2025-05-15 22:10:15.002500
#
# mi_fecha = mi_fecha.replace(month=11)  # Remplaza un valor puntal
# print(mi_fecha)  # 2025-11-15 22:10:15.002500
#
# from datetime import date
#
# nacimiento = date(1995, 3, 5)
# defuncion = date(2095, 6, 19)
#
# vida = defuncion - nacimiento
# print(vida.days)
#
# from datetime import datetime
#
# despierta = datetime(2022, 10, 5, 7, 30)
# duerme = datetime(2022, 10, 5, 23, 45)
#
# vigilia = duerme - despierta
# print(vigilia.seconds)


