from part2 import bidiagonalize
from utils import assert_bidiagonal, assert_matrix_equal

import numpy as np

def test_bidiagonalize_result(eps=1e-7):
	print("Test bidiagonalize result...", end=" ")

	A = np.array([[2, 3, 8], [4, 6, 6], [7, 9, 3]])
	Qleft, BD, Qright = bidiagonalize(A)
	result = Qleft @ BD @ Qright

	assert_matrix_equal(A, result, eps)
	assert_bidiagonal(BD)
	print("\tOK")


def test_bidiagonalize_eye_result(N=10, eps=1e-7):
	print("Test bidiagonalize result on identity...", end=" ")

	A = np.eye(N)
	Qleft, BD, Qright = bidiagonalize(A)
	result = Qleft @ BD @ Qright

	assert_matrix_equal(A, result, eps)
	assert_bidiagonal(BD)
	print("\tOK")


def test_bidiagonalize_ones_result(N=10, M=15, eps=1e-7):
	print("Test bidiagonalize result on 1-filled matrix...", end=" ")

	A = np.ones((N, M))
	Qleft, BD, Qright = bidiagonalize(A)
	result = Qleft @ BD @ Qright

	assert_matrix_equal(A, result, eps)
	assert_bidiagonal(BD)
	print("\tOK")


def test_bidiagonalize_random_result(N=10, M=15, eps=1e-7):
	print("Test bidiagonalize result on random matrix...", end=" ")

	# Array with values between 0 and 1
	A = 2 * np.random.rand(N, M) - np.ones((N, M))
	Qleft, BD, Qright = bidiagonalize(A)
	result = Qleft @ BD @ Qright

	assert_matrix_equal(A, result, eps)
	assert_bidiagonal(BD, eps)
	print("\tOK")


if __name__ == '__main__':
	N = 10
	M = 15
	eps = 1e-7
	test_bidiagonalize_result(eps)
	test_bidiagonalize_eye_result(N, eps)
	test_bidiagonalize_ones_result(N, M, eps)
	test_bidiagonalize_random_result(N, M, eps)