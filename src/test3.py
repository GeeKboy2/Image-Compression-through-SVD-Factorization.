from part3 import diagonalize, QR, SVD
from utils import assert_diagonal, assert_matrix_equal, assert_upper_triangular, assert_orthogonal

import numpy as np

def test_diagonalize_result(bi_diag, n_max, eps=1e-7):
	print("Test diagonalize result...", end=" ")

	u, res, v = diagonalize(bi_diag, n_max)

	assert_matrix_equal(bi_diag, u @ res @ v, eps)
	assert_diagonal(res, eps)
	print("\tOK")


def test_qr_decomposition_result(n, m, eps=1e-7):
	print("Test QR decomposition result (random matrix)...", end=" ")

	a = np.random.randn(n, m)

	q, r = QR(a)

	assert_upper_triangular(r, eps)
	assert_orthogonal(q, eps)
	assert_matrix_equal(q @ r, a, eps)

	print("\tOK")


def test_svd_result(n, m, n_max, eps=1e-7):
	print("Test SVD result (random matrix)...", end=" ")

	a = np.random.randn(n, m)

	l, d, r = SVD(a, n_max)
	
	size = min(n, m)
	S = np.zeros((n, m))
	np.fill_diagonal(S[:size, :size], d)

	assert_matrix_equal(l @ S @ r, a, eps)

	print("\tOK")


if __name__ == '__main__':
	n, m = 5, 6
	n_max = 100
	eps = 1e-4

	a = 3 * np.eye(n) + 2 * np.eye(n, k=1)

	test_qr_decomposition_result(n, n, eps) # Square matrix
	test_qr_decomposition_result(n, m, eps)
	test_diagonalize_result(a, n_max, eps)
	test_svd_result(n, n, n_max, eps) # Square matrix
	test_svd_result(n, m, n_max, eps)