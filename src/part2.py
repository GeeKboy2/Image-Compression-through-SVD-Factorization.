from part1 import householder

import numpy as np

def compute_Q1(BD, i, n):
	U = BD[i:, i]
	V = np.zeros(n - i)
	V[0] = np.linalg.norm(U)

	H, _ = householder(U, V)

	Q1 = np.eye(n)
	Q1[i:, i:] = H
	return Q1


def compute_Q2(BD, i, m):
	U = BD[i, i + 1:]
	V = np.zeros(m - i - 1)
	V[0] = np.linalg.norm(U)
	
	H, _ = householder(U, V)
	
	Q2 = np.eye(m)
	Q2[i + 1:, i + 1:] = H
	return Q2


def bidiagonalize(A):
	"""
	Returns Qleft, BD, Qright in the following equation, 
	where Qleft and Qright are orthogonal and BD bidiagonal :
	A = Qleft * BD * Qright
	"""
	n, m = A.shape
	Qleft = np.eye(n)
	Qright = np.eye(m)
	BD = A.copy()

	for i in range(min(n, m)):
		Q1 = compute_Q1(BD, i, n)
		Qleft = Qleft @ Q1
		BD = Q1 @ BD

		if i < m - 2 :
			Q2 = compute_Q2(BD, i, m)
			Qright = Q2 @ Qright
			BD = BD @ Q2
	return Qleft, BD, Qright


if __name__ == '__main__':
	pass