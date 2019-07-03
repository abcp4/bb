import numpy as np
import load
#queremos maximizar:
def f(x,S,c,m):
    val = 0
    for i in range(len(x)):
        if(x[i]==1):
            val+= c[i]
            #print(val)
    return val

S,c = load.loadFile("nl01-40.txt")
m = len(S)
print('m: ',m)
print('S')
#A mascara boolena que queremos encontrar
x = np.asarray([0,0,0,0,0,1,0,1])
v = f(x,S,c,m)
print(v)