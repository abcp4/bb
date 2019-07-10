import numpy as np
import bb
import load
import copy

#passo 1: ler dados do arquivo a ser testado
#passo 2: aplicar branch and bound
#passo 3: retornar resultado

length_of_x, conjuntos_de_x, coeficientes = load.loadFileEx("../inputs/nl01-40.txt")


def branch_and_bound():
    print(length_of_x)
    initial_x_set = create_initial_x_set(length_of_x)
    
    array_de_nos = []
    array_de_nos.append(initial_x_set)
    
    relax_function_value = relax_function(conjuntos_de_x, coeficientes)
    max_value = relax_function_value
    max_set = []
    
    x = 1
    last_x = length_of_x
    
    initial_bound = -1000
    max_quantidade_de_x = 4 

    while(x <= last_x) and (len(array_de_nos) > 0):
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
            #print(max_value)
            #print(f_result)
            #print(max_set)
            #print(set)
            if max_value == f_result:
                print("Substitute")
                max_set = copy.deepcopy(set)
                print("new max_set")
                print(max_set)
            print("---------------------------------")
            
        length_set = len(array_de_nos)
        i = 0
        #da pra melhorar essa parte para nao ter que fazer DOIS calculos seguindos
        while (i < len(array_de_nos)):
            if (bb.resultado_de_soma(array_de_nos[i], conjuntos_de_x, coeficientes, length_of_x) < initial_bound):
                print(bb.resultado_de_soma(array_de_nos[i], conjuntos_de_x, coeficientes, length_of_x))
                array_de_nos.remove(array_de_nos[i])
                initial_bound = initial_bound+1
            elif (quant_of_x(array_de_nos[i]) > max_quantidade_de_x):
                print(array_de_nos[i])
                #array_de_nos.remove(array_de_nos[i])
                del array_de_nos[i]
            else: i = i+1
        x = x+1
        
    print(max_set)
    print(bb.resultado_de_soma(max_set, conjuntos_de_x, coeficientes,length_of_x))
    
def create_initial_x_set(n):
    x_set = np.zeros(n+1)
    #print(type(x_set))
    return x_set 

def relax_function(x_sets,coeficientes):
    #maximo valor entre primeiro conjunto disponivel e 0
    first_coeficient_of_sets_available = 0
    for i in range(len(x_sets)):
        if (x_sets[i][0] == 1):
            first_set_available = coeficientes[i]
            break
    return max(0, first_coeficient_of_sets_available)

def quant_of_x(array):
    quant = 0
    i = 0
    length_of_x = len(array)
    while (i < length_of_x):
        quant += array[i]
        i = i+1
    return quant

branch_and_bound()