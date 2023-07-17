import time
import os
# time.sleep(1) # añade un retraso de 500 ms
segundo = 59
minuto = 59
hora = 24

while segundo < 60:
    if 0 > hora > 24 :
        hora = 0
        minuto = 0
        segundo = 0
    else:
        print(f"{hora}:{minuto}:{segundo}")
        segundo = segundo + 1
        time.sleep(1)
        os.system('cls')
        if segundo == 60:
            minuto = minuto + 1
            segundo = 0
            if minuto == 60:
                segundo = 0
                minuto = 0
                hora = hora + 1
                if hora == 24:
                    segundo = 0
                    minuto = 0
                    hora = 0

