import numpy as np
import bb
import load
import copy
import math

#passo 1: ler dados do arquivo a ser testado
#passo 2: aplicar branch and bound
#passo 3: retornar resultado

length_of_x = 0
conjuntos_de_x = []
coeficientes = []

def branch_and_bound(entrada):
    global length_of_x, conjuntos_de_x, coeficientes
    length_of_x, conjuntos_de_x, coeficientes = load.loadFileEx(entrada)

    conjuntos_de_x, coeficientes = order_conjuntos_e_coeficientes(length_of_x,conjuntos_de_x,coeficientes)
    #print(conjuntos_de_x)

    initial_x_set = create_initial_x_set(length_of_x)
    
    array_de_nos = create_initial_array_de_nos_best_fit()
    
    lower_bound = create_initial_max_value()
    max_set = []
      
    x = 1
    last_x = length_of_x

    while(x <= last_x) and (len(array_de_nos) > 0):
        print ("x atual e " + str(x) + " | max value e " + str(lower_bound) + " | set size e " + str(len(array_de_nos)))
        if (x == 2): print (array_de_nos)
        novo_set = []
        
        for set in array_de_nos:
            set_inverted = copy.deepcopy(set)
            if (set_inverted[x] == 1):
                set_inverted[x] = 0
            else:
                set_inverted[x] = 1
            novo_set.append(set_inverted)
            same_set = copy.deepcopy(set)
            novo_set.append(same_set)
        
        array_de_nos = novo_set
        
        for set in array_de_nos:
            f_result = bb.resultado_de_soma(set, conjuntos_de_x, coeficientes, length_of_x)
            lower_bound = max(lower_bound, f_result)
            #print(str(set) + " " + str(f_result) + " " + str(lower_bound))
            #print(max_set)
            #print(set)
            if lower_bound == f_result:
                #print("Substitute")
                max_set = copy.deepcopy(set)
                #print("new max_set")
                #print(max_set)
            #print("---------------------------------")

        array_de_nos = apply_bound(array_de_nos)
        x = x+1
        
    #print(max_set)
    #print(bb.resultado_de_soma(max_set, conjuntos_de_x, coeficientes,length_of_x))
    return max_set, bb.resultado_de_soma(max_set, conjuntos_de_x, coeficientes,length_of_x)

def order_conjuntos_e_coeficientes(length_of_x,old_conjuntos_de_x,old_coeficientes):
    
    '''
    Separa valores de coeficientes 1
    Coloca eles no comeco dos novos arrays de conjunto de x e coeficiente
    Ordena os outros em ordem de menor pra maior
    retorna tudo
    '''

    new_conjuntos_de_x = old_conjuntos_de_x[0:length_of_x]
    new_coeficientes = old_coeficientes[0:length_of_x]
    
    array_size = len(old_conjuntos_de_x)
    temp_conjuntos_de_x = old_conjuntos_de_x[length_of_x:array_size]
    temp_coeficientes = old_coeficientes[length_of_x:array_size]
    
    
    class Templine:
        def __init__(self, coef, conjunto_de_x):
            self.coef = coef
            self.conjunto_de_x = conjunto_de_x
    
    temp_joined_list = []
    i = 0
    while (i < len(temp_coeficientes)):
        temp_joined_list.append(Templine(temp_coeficientes[i], temp_conjuntos_de_x[i]))
        i = i+1
    
    temp_joined_list.sort(key=lambda x: x.coef, reverse=True)
    #print(temp_joined_list)
    
    new_conjuntos_de_x = new_conjuntos_de_x.tolist()
    
    i = 0
    while (i < len(temp_joined_list)):
        new_conjuntos_de_x.append(list(temp_joined_list[i].conjunto_de_x))
        new_coeficientes = np.append(new_coeficientes, temp_joined_list[i].coef)
        i= i+1
    
    return new_conjuntos_de_x,new_coeficientes
    
    
def create_initial_x_set(n):
    
    x_set = np.zeros(n+1)
    #print(type(x_set))
    return x_set 

def create_initial_array_de_nos_best_fit():
    
    array_de_nos = []
 
    i = 0  
    limite = len(conjuntos_de_x)
    #print(conjuntos_de_x)

    maior_coef = -math.inf
    while (i < limite):
        maior_coef = max(maior_coef, coeficientes[i])
        i = i+1
    
    #print("Maior coef: " + str(maior_coef))
    #print (length_of_x)
    #print(coeficientes[0:10])
    
    if (maior_coef < 0):
        i = length_of_x
        j = 1
        k = 2
        while (j < length_of_x):
            while(k <= length_of_x) and (i < limite):
                if (conjuntos_de_x[i][0] > 1):
                    if (conjuntos_de_x[i][1] == j) and (conjuntos_de_x[i][2] == k):
                        i += 1
                    elif (conjuntos_de_x[i][1] == j) and (conjuntos_de_x[i][2] != k):
                        new_set = create_initial_x_set(length_of_x)
                        new_set[j] = 1
                        new_set[k] = 1
                        #print(str(j) + " " + str(k))
                        #print("---")
                        array_de_nos.append(copy.deepcopy(new_set))
                    k += 1
                elif (i >= limite): break
            j += 1
            k = j+1
            if (i >= limite): break
            
    else:
        i = 0
        while (i < limite):
            if (maior_coef == coeficientes[i]):
                #print (conjuntos_de_x[i])
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

def teste():
    conjunto, resultado = branch_and_bound("../inputs/nl01-40.txt")
    print (conjunto)
    print (resultado)
    
teste()