import numpy as np
import load
#queremos maximizar:
def resultado_de_soma(x,S,c,m):
    val = 0
    for i in range(len(x)):
        if(x[i]==1):
            val+= c[i]
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