import numpy as np
def loadFile(file):
	S = []
	c = []#coeficientes dos produtos

	f = open(file, "r")
	i = 0
	for x in f:
		#print(x)
		i+=1
		if(i<3):
			continue
		#print(x) 
		elems = x.split(' ')
		#print(elems)
		elems = elems[2:]
		#remove \n from last char
		elems[-1]=elems[-1][:-1]
		#print(elems)
		for j in range(len(elems)):
			elems[j] = float(elems[j])
		#print(elems)

		c.append(elems[0]) #coef para cada item	
		S.append(elems[1:])#S1,..,Sm
	 
	S = np.asarray(S)
	#coeficientes
	c = np.asarray(c)
	#print(S)
	#print(c)
	
	return S,c
	