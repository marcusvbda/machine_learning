import numpy as np

melancia = 0
maca = 1
uva = 2

vermelho = 0 
verde = 1
roxo = 2

pequeno = 0
medio = 1
grande = 2

# amostra
X = np.array(
[
		[verde, grande], 
		[verde, pequeno], 
		[vermelho, medio], 
		[vermelho, pequeno], 
		[roxo, pequeno],
		[verde, medio],
		[vermelho, grande],
])

# respostas
Y = np.array([
		melancia,
		uva ,
		maca, 
		maca, 
		uva,
		uva,
		melancia
])


from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X, Y)


result = clf.predict([[vermelho, grande]])

if result == 0:
	print("melancia")
elif result == 1:
	print("maçã")
elif result == 2:
	print("uva")

