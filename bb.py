import numpy as np
import load
#queremos maximizar:
def f(x,S,c,m):
	#aplica-se a mascara sobre as variaveis
	val = 0
	for i in range(m):
		# a mascara tem que ir só até o tamanho dos valores
		mult = 1
		print(S[i])
		for j in range(len(S[i])):
			if(x[j]==1):
				print('S[i][j]:',S[i][j])
				mult*=S[i][j]
		print(mult)
		print(c[i])
		val+= c[i]*mult
		print(val)
		a = 2/0
	return val

S,c = load.loadFile("nl01-40.txt")
m = len(S)
print('m: ',m)
#A mascara boolena que queremos encontrar
x = np.asarray([1,1,1,1])
v = f(x,S,c,m)
print(v)
