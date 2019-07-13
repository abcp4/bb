from __future__ import print_function
import math
import random
from anneal import Annealer

import numpy as np
import load


def create_initial_x_set(n):
    x_set = np.zeros(n)
    return x_set 


class WMaxSat(Annealer):
    def __init__(self, state, conjuntos_de_x,coefs,size= 31, vars_num = 2, mode = 1):
        self.conjuntos_de_x = conjuntos_de_x
        self.coefs = coefs
        self.size = size
        #para casos de bqp, vars_num = 50 e mode = 2
        self.vars_num = 2
        self.mode = mode

        super(WMaxSat, self).__init__(state)  # important!

    def move(self):
        a = np.zeros(self.size)
        if(self.mode ==1):
          for i in range(self.vars_num):
              x = random.randint(0,self.size-1)
              if(a[x]==0):
                  a[x] = 1
              else:
                  a[x] = 0
        elif(self.mode==2):
          a = np.random.randint(2, size=self.size-1)
        #print('state:',a)
        self.state = a.tolist()


    #queremos maximizar:
    def energy(self):
        x = self.state
        #print('x:',x)
        conjuntos_de_x = self.conjuntos_de_x
        coefs = self.coefs
        m = self.size
        conjunto_de_x_a_testar= x+ [0 for i in range(m)]
        soma = 0
        i = 0
        while i < len(conjuntos_de_x):
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
        return -soma


def teste(endereco):

    length, conjuntos_de_x,coeficientes = load.loadFileEx(endereco)#mode 1 se for a snovas instancias
    length += 1
    m = len(conjuntos_de_x)
    initial_x_set = create_initial_x_set(length)
    array_de_nos = []
    array_de_nos.append(initial_x_set)

    init_state = np.zeros(length)
    init_state = init_state.tolist()

    #print(length)
    tsp = WMaxSat(init_state, conjuntos_de_x,coeficientes,size = length)
    tsp.steps = 1000
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()
    e = -e
    #print("OVER!!")
    #print('state: ',np.argwhere(np.asarray(state) > 0))
    #print('e: ',e)
    return np.argwhere(np.asarray(state) > 0), e