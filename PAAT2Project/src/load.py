import numpy as np

def loadFile(file):
    S = []
    c = []#coeficientes dos produtos

    resultado_de_soma = open(file, "r")
    i = 0
    for x in resultado_de_soma:
        #print(x)
        i+=1
        if(i<3):
            continue
        #print(x) 
        elems = x.split(' ')
        #print(elems)
        elems = elems[2:]
        #remove \n from last char
        elems[-1]=elems[-1][:-1]
        #print(elems)
        for j in range(len(elems)):
            elems[j] = float(elems[j])
        #print(elems)

        c.append(elems[0]) #coef para cada item    
        S.append(elems[1:])#S1,..,Sm
     
    S = np.asarray(S)
    #coeficientes
    c = np.asarray(c)
    #print(S)
    #print(c)
    
    return S,c

def loadFileEx(file):
    conjuntos_de_x = []
    coeficientes = []#coeficientes dos produtos
    quant_de_x = 0
    
    resultado_de_soma = open(file, "r")
    i = 0
    for x in resultado_de_soma:
        #print(x)
        i+=1
        if(i<3):
            if (i == 1):
                elems = x.split(' ')
                quant_de_x = int(elems[0])
            continue
        #print(x) 
        elems = x.split(' ')
        #print(elems)
        if (elems[1] == ''):
            elems = elems[2:]
        else:
            elems = elems[1:]
        #remove \n from last char
        elems[-1]=elems[-1][:-1]
        #print(elems)
        for j in range(len(elems)):
            elems[j] = float(elems[j])
        #print(elems)
        #print(elems[0])
        #print(elems[1:])

        coeficientes.append(elems[0]) #coef para cada item    
        conjuntos_de_x.append(elems[1:])#S1,..,Sm
     
    conjuntos_de_x = np.asarray(conjuntos_de_x)
    #coeficientes
    coeficientes = np.asarray(coeficientes)
    #print(conjuntos_de_x)
    #print(coeficientes)
    
    return quant_de_x,conjuntos_de_x,coeficientes

#loadFileEx("../inputs/nl01-40.txt")
#loadFileEx("../inputs/bqp50-1.txt")