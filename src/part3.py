from part1 import householder, matrix_product_left, matrix_product_right
from part2 import bidiagonalize

import numpy as np

def QR(BD):
	"""
	Returns Q, R in the following equation, where
	Q is orthogonal, R upper triangular, and BD bidiagonal :
	BD = Q * R
	"""
	n, m = BD.shape
	Q = np.eye(n)
	R = BD.copy()

	for i in range(min(n, m)):

		U = R[i:, i]
		V = np.zeros(n - i)
		V[0] = np.linalg.norm(U)
		H, N = householder(U, V)
		
		R[i:, :] = matrix_product_right(H, N, R[i:, :]) #R = H @ R
		Q[:, i:] = matrix_product_left(H, N, Q[:, i:]) #Q = Q @ H

	return Q, R


def diagonalize(BD, n_max):
	"""
	Returns U, S, V in the following equation, where
	U and V are both orthogonal, S diagonal and BD bidiagonal :
	BD = U * S * V
	"""
	n, m = BD.shape
	U, V = np.eye(n), np.eye(m)
	res = BD.copy()

	for _ in range(n_max):
		Q1, R1 = QR(res.T) # Originally np.linalg.qr
		Q2, R2 = QR(R1.T) # Originally np.linalg.qr

		res = R2
		U = U @ Q2
		V = Q1.T @ V
	
	return U, res, V


def diag_convergence(BD, n_max):
	"""
	Helper function which allows to show the convergence
	of the diagonalize function
	"""
	n = len(BD)
	U, V = np.eye(n), np.eye(n)
	res = BD.copy()

	_, expected, _ = diagonalize(BD, n_max)
	norms = []

	for _ in range(n_max):
		Q1, R1 = QR(res.T) # Originally np.linalg.qr
		Q2, R2 = QR(R1.T) # Originally np.linalg.qr

		res = R2
		U = U @ Q2
		V = Q1.T @ V
		
		norms.append(np.linalg.norm(res - expected) / np.linalg.norm(res))
	
	return norms


def SVD(A, n_max):
	"""
	Singular Value Decomposition (SVD) using the Householder method

	Returns X, dS, Y in the following equation, 
	where X and Y are both orthogonal matrices, S a diagonal matrix, 
	and A any matrix (dS stands for the diagonal of S) :
	A = X * S * Y

	n_max allows to specify an iteration count for the diagonalize function
	"""
	Qleft, BD, Qright = bidiagonalize(A) # Qleft * BD * Qright = A
	U, S, V = diagonalize(BD, n_max) # U * S * V = BD

	D = np.diag(S)
	idx = np.argsort(D)[::-1]
	U = U[idx, :]
	D = D[idx]

	return Qleft @ U, D, V @ Qright


if __name__ == '__main__':
	import matplotlib.pyplot as plt

	n = 4
	n_max = 100
	a = np.random.rand(n) * np.eye(n) + np.random.rand(n) * np.eye(n, k=1)
	
	norms = diag_convergence(a, n_max)
	x = [k for k in range(n_max)]

	plt.title("Vitesse de convergence\nPassage d'une matrice bi-diagonale à une matrice diagonale")
	plt.grid()
	plt.xlabel("Nombre d'itérations")
	plt.ylabel("Norme de la différence")
	plt.plot(x, norms)

	plt.show()