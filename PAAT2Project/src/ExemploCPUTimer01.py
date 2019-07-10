# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 12:04:09 2016
@author: Psyny
"""

import CPUTimer

# Fun��o a ser cronometrada:
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
    
# Instanciano a CPU timer  
timer = CPUTimer.CPUTimer()


# Medindo c�digo curto/rapido executando diversas vezes
print("")
print("Medindo codigo r�pido repetido diversas vezes:")
timer.reset()
timer.start()
for i in range(0, 100000):  
    fib(10)
    timer.lap()
timer.stop()
# Imprimindo resultados de diversas formas
print("Tempo Total: " + str( timer.get_time() ) +" s")
print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )


# Medindo c�digo longo/pesado repetido uma unica vez
print("")
print("Medindo codigo longo/pesado repetido uma vez:")
timer.reset()
timer.start()
fib(35)
timer.stop()
# Imprimindo resultados de diversas formas
print("Tempo Total: " + str( timer.get_time() ) +" s")
print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )


# Outros exemplos de exibi��o
print("\n\nOutros exemplos de exibi��o de resultados:")
print("\nEstampa que ignora zeros:")
print( timer.get_stamp("total","si",True) )
print( timer.get_stamp("total","clock",True) )
