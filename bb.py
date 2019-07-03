import numpy as np
#queremos maximizar:
def f(x,S,c):
	#aplica-se a mascara sobre as variaveis
	val = 0
	for i in range(m):
		S1 = S[i]*x
		val+= c[i]*S1
	return val

#produtos sao da forma c*m
m = 5 #numero de produtos
c = []#coeficientes dos produtos

#variaveis
S = []
for i in range(m):
	#esses valores recebemos nas instancias
	#preenchendo com valores quaisquer...
    S.append([4,10,5,1])#S1,..,Sm
    c.append(1) #coef para cada item


S = np.asarray(S)
#coeficientes
c = np.asarray(c)

#A mascara boolena que queremos encontrar
x = np.asarray([0,0,0,1])

v = f(x,S,c)
print(v)