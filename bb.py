import numpy as np
import load
#queremos maximizar:
def f(x,S,c,m):
	#aplica-se a mascara sobre as variaveis
	val = 0
	for i in range(m):
		# a mascara tem que ir só até o tamanho dos valores
		mult = 1
		#print(S[i])
		for j in range(len(S[i])):
			if(x[j]==1):
				mult*=S[i][j]
		val+= c[i]*mult
		#print(val)
	return val

S,c = load.loadFile("nl01-40.txt")
m = len(S)
print('m: ',m)
#A mascara boolena que queremos encontrar
x = np.asarray([1,1,1,1])
v = f(x,S,c,m)
print(v)
