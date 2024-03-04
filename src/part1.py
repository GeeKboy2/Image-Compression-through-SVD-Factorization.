import numpy as np

def compute_N(U, V):
	"""
	Returns the column matrix N resolving the following equation :
	V = U - 2 * N * N^T * U
	"""
	if np.array_equal(U, V):
		return None
	diff = U - V
	res = diff / np.linalg.norm(diff)
	return res.reshape(len(U), 1)


def householder(U, V):
	"""
	Returns (H, N) in the matrix equation H.U = V
	with H = Id - 2 * N * N^T
	"""
	N = compute_N(U, V)
	identity = np.eye(len(U))
	
	if N is None:
		return identity, None
	return identity - 2 * (N @ N.T), N


def vector_product(H, N, V):
	"""
	Returns the product H * V, with only a dot product (using N)
	Note H is useless here, except it shows we are dealing with a HH matrix
	"""
	if N is None:
		return V
	alpha = N.T @ V # Scalar product
	return V - 2 * alpha * N


def matrix_product_right(H, N, VL):
	"""
	Returns the matrix product H * VL, using scalar products
	Note H is useless here, except it shows we are dealing with a HH matrix
	"""
	if N is None:
		return VL

	n = VL.shape[1]
	factors = np.zeros(n)

	for k in range(n):
		factors[k] = N.T @ VL[:, k] # Scalar product
	return VL - 2 * N * factors


def matrix_product_left(H, N, VL):
	"""
	Returns the matrix product VL * H, using scalar products
	Note H is useless here, except it shows we are dealing with a HH matrix
	"""
	if N is None:
		return VL
	
	n = VL.shape[0]
	factors = np.zeros(n)

	for k in range(n):
		factors[k] = VL[k, :] @ N # Scalar product
	return VL - 2 * factors.reshape((n, 1)) @ N.T


if __name__ == '__main__':
	import matplotlib.pyplot as plt
	import time

	sizes = np.arange(50, 4000, 300)

	vt = []
	vt_opt = []
	mt = []
	mt_opt = []

	for n in sizes:
		A = np.random.randn(n, n)
		V = np.random.randn(n)
		N = np.ones(n)

		start = time.time()
		vector_product(A, N, V)
		vt_opt.append(time.time() - start)

		start = time.time()
		A @ V
		vt.append(time.time() - start)

		start = time.time()
		matrix_product_right(A, N, A)
		mt_opt.append(time.time() - start)

		start = time.time()
		A @ A
		mt.append(time.time() - start)

	plt.subplot(1, 2, 1)	
	plt.plot(sizes, vt_opt, label='Version optimisée')
	plt.plot(sizes, vt, label='Version naïve')
	plt.title('Produit par un vecteur')
	plt.xlabel('Taille de la matrice')
	plt.ylabel('Temps de calcul en s')
	plt.legend()
	plt.grid()

	plt.subplot(1, 2, 2)
	plt.plot(sizes, mt_opt, label='Version optimisée')
	plt.plot(sizes, mt, label='Version naïve')
	plt.title('Produit par une matrice')
	plt.xlabel('Taille de la matrice')
	plt.ylabel('Temps de calcul en s')
	plt.legend()
	plt.grid()
	
	plt.tight_layout()
	plt.show()

