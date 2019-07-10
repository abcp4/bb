import numpy as np
import bb
import load
import copy
import math

#passo 1: ler dados do arquivo a ser testado
#passo 2: aplicar branch and bound
#passo 3: retornar resultado

length_of_x, conjuntos_de_x, coeficientes = load.loadFileEx("../inputs/nl01-40.txt")

print(length_of_x)

def branch_and_bound():
    print(length_of_x)
    initial_x_set = create_initial_x_set(length_of_x)
    
    array_de_nos = create_initial_array_de_nos()
    
    max_value = create_initial_max_value()
    max_set = []
      
    x = 1
    last_x = length_of_x

    while(x <= last_x) and (len(array_de_nos) > 0):
        print ("x atual e " + str(x))
        novo_set = []
        
        print(x)
        
        for set in array_de_nos:
            set_with = copy.deepcopy(set)
            set_with[x] = 1
            novo_set.append(set_with)
            set_without = copy.deepcopy(set)
            novo_set.append(set_without)
        
        array_de_nos = novo_set
        
        for set in array_de_nos:
            f_result = bb.resultado_de_soma(set, conjuntos_de_x, coeficientes, length_of_x)
            max_value = max(max_value, f_result)
            print(max_value)
            #print(f_result)
            #print(max_set)
            #print(set)
            if max_value == f_result:
                #print("Substitute")
                max_set = copy.deepcopy(set)
                #print("new max_set")
                #print(max_set)
            #print("---------------------------------")

        array_de_nos = apply_bound(array_de_nos)
        x = x+1
        
    print(max_set)
    print(bb.resultado_de_soma(max_set, conjuntos_de_x, coeficientes,length_of_x))
    
def create_initial_x_set(n):
    
    x_set = np.zeros(n+1)
    #print(type(x_set))
    return x_set 

def create_initial_array_de_nos():
    
    array_de_nos = []
 
    i = length_of_x   
    limite = len(conjuntos_de_x)

    maior_coef = -math.inf
    while (i < limite):
        if (conjuntos_de_x[i][0] > 1):
            maior_coef = max(maior_coef, coeficientes[i])
        i = i+1
    
    i = length_of_x
    while (i < limite):
        if (conjuntos_de_x[i][0] > 1) and (maior_coef == coeficientes[i]):
            set = create_initial_x_set(length_of_x)
            j = 1
            while(j < len(conjuntos_de_x[i])):
                set[int(conjuntos_de_x[i][j])] = 1
                j = j+1
            array_de_nos.append(set)
        i = i+1    
    
    return array_de_nos

def create_initial_max_value():
    return 0

def higher_bound(set, x):
    #soma dos coeficientes positivos de um so x e 0 que nao foram testados
    #+ valores ja testados
    value = 0
    i = 0
    while (i < length_of_x(conjuntos_de_x)):
        if (conjuntos_de_x[i][0] > 1): break
        xi = conjuntos_de_x[i][1]
        if (xi < x):
            value += set[xi] * coeficientes[i][0]
        else:
            if (coeficientes[i][0] > 0): value += set[xi] * coeficientes[i][0]
        i += 1
    
    return value

def apply_bound(array_de_nos):
    quant = len(array_de_nos)
    i = 0
    soma = 0
    while (i < quant):
        soma += bb.resultado_de_soma(array_de_nos[i], conjuntos_de_x, coeficientes, length_of_x)
        i += 1
    media = soma / quant
    i = 0
    while (i < quant):
        if bb.resultado_de_soma(array_de_nos[i], conjuntos_de_x, coeficientes, length_of_x) < media:
            del array_de_nos[i]
            quant = len(array_de_nos)
        else: i += 1
    return array_de_nos

def quant_of_x(array):
    quant = 0
    i = 0
    length_of_x = len(array)
    while (i < length_of_x):
        quant += array[i]
        i = i+1
    return quant

branch_and_bound()