import numpy as np
import load

#passo 1: ler dados do arquivo a ser testado
#passo 2: aplicar branch and bound
#passo 3: retornar resultado

x_sets,coeficientes = load.loadFile("../inputs/nl01-40.txt")
x_size = 30 #precisamos que load.loadFile também retorne quantos x existem

length = len(x_sets)

def branch_and_bound():
    array_de_nos = []
    initial_x_set = create_initial_x_set(x_size)
    
    array_de_nos.append(initial_x_set)
    relax_function_value = relax_function
    initial_x = 0
    last_x = length-1
    
    
    #loop de branch and bound
    
    #return
    
def create_initial_x_set(n):
    x_set = np.zeros(n)
    return x_set 

def relax_function(x_sets,coeficientes):
    #maximo valor entre primeiro conjunto disponível e 0
    first_coeficient_of_sets_available = 0
    for i in range(len(x_sets)):
        if (x_sets[i][0] == 1):
            first_set_available = coeficientes[i]
            break
    return max(0, first_coeficient_of_sets_available)
    