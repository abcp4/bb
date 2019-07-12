import numpy as np
import load



#queremos maximizar:
def resultado_de_soma(x,conjuntos_de_x,coefs,m,relax=False):
    conjunto_de_x_a_testar= x+ [0 for i in range(m)]
    soma = 0
    i = 0
    while i < len(conjuntos_de_x):
        if(relax and coefs[i]<0):
            i = i+1
            continue
        j = 1
        somar = False
        #print(conjuntos_de_x[i])
        while j < len(conjuntos_de_x[i]):
            index = conjuntos_de_x[i][j]
            index = int(index)
            #print('index:',index)
            if conjunto_de_x_a_testar[index] == 1:
                somar = True
                #print('index:',index)
            else:
                somar = False
                break
            j = j+1
        if (somar):
            soma += coefs[i]
        i = i+1
    return soma

def test():
    S,c = load.loadFile("nl01-40.txt")
    print('S')
    #A mascara boolena que queremos encontrar
    #2,3,6,8
    x = [0 for i in range(10)]
    x[6] = 1
    x[8] = 1
    v = resultado_de_soma(x,S,c,31,relax=True)
    print(v)

def relax_function(x_sets,coeficientes):
    #maximo valor entre primeiro conjunto disponivel e 0
    first_coeficient_of_sets_available = 0
    for i in range(len(x_sets)):
        if (x_sets[i][0] == 1):
            first_coeficient_of_sets_available = coeficientes[i]
            break
    #print(first_coeficient_of_sets_available)
    return max(0, first_coeficient_of_sets_available)

def create_initial_x_set(n):
    x_set = np.zeros(n)
    return x_set 
 
length = 31
global conjuntos_de_x,coeficientes, m
conjuntos_de_x,coeficientes = load.loadFile("nl01-40.txt")
m = len(conjuntos_de_x)
initial_x_set = create_initial_x_set(length)
array_de_nos = []
array_de_nos.append(initial_x_set)

relax_function_value = relax_function(conjuntos_de_x, coeficientes)
max_value = relax_function_value
max_set = []

x = 0
last_x = length-1



#--------------------------------------
# enumera 0-1
#--------------------------------------
import copy

best_val = -9999999999
best_set = None

#o quanto voce ainda pode ganhar
def best_estimate(r,v):
  if(sum(v)==2):
    return 0
  
def update_estimate(v,opt,conjuntos_de_x,coeficientes):
	csum = 0
	for c in coeficientes:
		if(c>0):
			csum+=c 
	return csum
  
  
def enumer_01(v, l, lmax,optimistic_estimate,relax=False):
    global best_val
    global best_set


    if(l <= lmax and sum(v)<2):
        
        v.append(0)
        optimistic_estimate = update_estimate(v,optimistic_estimate,conjuntos_de_x,coeficientes)
        #print(v)
        result =resultado_de_soma(v,conjuntos_de_x,coeficientes,31,relax)
        
        if(result>best_val):
            best_val = result
            best_set = copy.deepcopy(v)
            print("New Best Solution value: ",best_val)
            print("Solution: ",best_set)
            
        #checa se ainda vale a pena fazer busca nessa sub arvore 
        #if(optimistic_estimate<best_val):
        #  return
        enumer_01(v, l+1, lmax,optimistic_estimate) 
        v.pop()
        
        v.append(1)
        optimistic_estimate = update_estimate(v,optimistic_estimate,conjuntos_de_x,coeficientes)
        #print(v)
        result = resultado_de_soma(v,conjuntos_de_x,coeficientes,31,relax)
        if(result>best_val):
            best_val = result
            best_set = copy.deepcopy(v)
            print("New Best Solution value: ",best_val)
            print("Solution: ",best_set)
        
        #checa se ainda vale a pena fazer busca nessa sub arvore 
        #if(optimistic_estimate<best_val):
        #  return
        enumer_01(v, l+1, lmax,optimistic_estimate)
        v.pop()
        
    else:
        print(v)
        t=1
        
n = 30
w = []
import timeit

start_time = timeit.default_timer()

#uma estimativa otimistica é a maior soma de k coeficientes positivos considerados
k = 2
sorteds = np.sort(coeficientes)
optimistic_estimate=0
l  = len(sorteds)
for i in range(1,k+1):
  optimistic_estimate+=sorteds[l-i]
  
print('optimistic_estimate:',optimistic_estimate)
enumer_01(w, 1, n, optimistic_estimate,relax = True)#no relax 27-30
print(timeit.default_timer() - start_time)

print("Max Solution value: ",best_val)
print("Solution: ",best_set)