import numpy as np
import load
#queremos maximizar:
def resultado_de_soma(conjunto_de_x_a_testar,conjuntos_de_x,coefs,m):
    #para todos os conjuntos_de_x
    #para cada conjunto de x
    # somar = true
    # se conjunto_de_x_a_testar[conjunto_de_x[i]-1] == 1
    #    somar = true
    # else somar = false
    # if somar == true
    #val += coefs[i]
    val = 0
    for i in range(len(conjunto_de_x_a_testar)):
        if(conjunto_de_x_a_testar[i]==1):
            val+= coefs[i]
            #print(val)
    return val

def test():
    S,c = load.loadFile("../inputs/nl01-40.txt")
    m = len(S)
    print('m: ',m)
    print('S')
    #A mascara boolena que queremos encontrar
    #6,8
    x = np.zeros(30)
    x[3] = 1
    x[11] = 1
    v = resultado_de_soma(x,S,c,m)
    print(v)