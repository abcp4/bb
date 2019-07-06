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
    soma = 0
    i = 0
    while i < len(conjuntos_de_x):
        j = 0
        somar = False
        while j < len(conjuntos_de_x[i]):
            index = conjuntos_de_x[i][j]-1
            index = int(index)
            if conjunto_de_x_a_testar[index] == 1:
                somar = True
            else:
                somar = False
                break
            j = j+1
        if (somar):
            soma += coefs[i]
        i = i+1
    return soma

def test():
    S,c = load.loadFile("../inputs/nl01-40.txt")
    m = len(S)
    print('m: ',m)
    print('S')
    #A mascara boolena que queremos encontrar
    #2,3,6,8
    x = np.zeros(30)
    x[1] = 1
    x[2] = 1
    x[5] = 1
    x[7] = 1
    v = resultado_de_soma(x,S,c,m)
    print(v)
    
test()