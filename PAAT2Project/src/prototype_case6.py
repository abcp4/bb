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
        #if (x == 3): print (max_set)
        novo_set = []
        
        for set in array_de_nos:
            set_inverted = copy.deepcopy(set)
            if (set_inverted[x] == 1):
                set_inverted[x] = 0
            else:
                set_inverted[x] = 1
            if (upper_bound(set_inverted, x) > lower_bound):
                novo_set.append(set_inverted)
            same_set = copy.deepcopy(set)
            if (upper_bound(same_set, x) >= lower_bound):
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
    print(array_de_nos)
    return max_set, lower_bound

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
    
    size_of_coef_1 = coeficientes[0:length_of_x]
    maior_valor_inicial = -100000
    i = 0
    
    while (i < length_of_x):
        if (size_of_coef_1[i] > maior_valor_inicial):
            maior_valor_inicial = size_of_coef_1[i]
        i += 1
    
    return maior_valor_inicial

def upper_bound(set, x):
    #soma dos coeficientes positivos
    
    if (x == length_of_x): return float("inf")
    
    i = x+1
    while (i <= length_of_x):
        set[i] = 1
        i += 1
    
    value = 0
    i = 0
    isolated_x_length = length_of_x
    
    while (i < isolated_x_length):
        xi = int(math.floor(conjuntos_de_x[i][1]))
        if (coeficientes[i] > 0) and (set[xi] == 1):
            value += coeficientes[i]
        i += 1
    
    i = len(coeficientes) - 1
    
    while (coeficientes[i] > 0) and (conjuntos_de_x[i][0] == 2):
        xi = int(math.floor(conjuntos_de_x[i][1]))
        xii = int(math.floor(conjuntos_de_x[i][2]))
        if (set[xi] == 1) and (set[xii] == 1):
             value += coeficientes[i]
        i -= 1
        
    return value

def apply_bound(array_de_nos):
    quant = len(array_de_nos)
    i = 0
    melhor = -1000000
    segundo_melhor = -1000000
    while (i < quant):
        resultado =  bb.resultado_de_soma(array_de_nos[i], conjuntos_de_x, coeficientes, length_of_x)
        if (resultado >= melhor):
            segundo_melhor = melhor
            melhor = resultado
        i += 1
        
    i = 0
    peguei_melhor = False
    peguei_segundo_melhor = False
    array_novo_de_nos = []
    while (i < quant):
        if (bb.resultado_de_soma(array_de_nos[i], conjuntos_de_x, coeficientes, length_of_x) == segundo_melhor):
            array_novo_de_nos.append(array_de_nos[i])
        elif (bb.resultado_de_soma(array_de_nos[i], conjuntos_de_x, coeficientes, length_of_x) == melhor):
            array_novo_de_nos.append(array_de_nos[i])
        i += 1
    
    return array_novo_de_nos

def quant_of_x(array):
    quant = 0
    i = 0
    length_of_x = len(array)
    while (i < length_of_x):
        quant += array[i]
        i = i+1
    return quant

def teste():
    conjunto, resultado = branch_and_bound("../inputs/nl01-41.txt")
    print (conjunto)
    print (resultado)
    
teste()