from part1 import householder, vector_product, matrix_product_right, matrix_product_left
from utils import assert_vector_equal, assert_matrix_equal

import numpy as np

def test_householder_result(eps=1e-7):
	print("Test Householder result...", end=" ")
	
	U = np.array([[3], [4], [0]])
	V = np.array([[0], [0], [5]])

	result, _ = householder(U, V)
	expected = np.array([[0.64, -0.48, 0.6], [-0.48, 0.36, 0.8], [0.6, 0.8, 0]])

	assert_matrix_equal(result, expected, eps)
	print("\tOK")


def test_vector_product_result(eps=1e-7):
	print("Test vector product result...", end=" ")

	U = np.array([[3], [4], [0]])
	V = np.array([[0], [0], [5]])
	H, N = householder(U, V)

	W = np.array([[1], [2], [3]])
	result = vector_product(H, N, W)
	expected = H @ W

	assert_vector_equal(result, expected, eps)
	print("\tOK")


def test_matrix_product_result(eps=1e-7):
	print("Test matrix product result...", end=" ")

	U = np.array([[3], [4], [0]])
	V = np.array([[0], [0], [5]])
	H, N = householder(U, V)

	W = np.array([[0, 1, 0], [0, 2, 0], [0, 3, 0]])
	result = matrix_product_right(H, N, W)
	expected = H @ W
	assert_matrix_equal(result, expected, eps)

	W = np.array([[0, 0, 1], [0, 0, 2], [0, 0, 3]])
	result = matrix_product_right(H, N, W)
	expected = H @ W
	assert_matrix_equal(result, expected, eps)

	W = np.array([[0, 1, 1], [0, 2, 2], [0, 3, 3]])
	result = matrix_product_right(H, N, W)
	expected = H @ W
	assert_matrix_equal(result, expected, eps)

	W = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
	result = matrix_product_right(H, N, W)
	expected = H @ W
	assert_matrix_equal(result, expected, eps)

	print("\tOK")


def test_matrix_product_left_result(eps=1e-7):
	print("Test matrix product (on the left) result...", end=" ")

	U = np.array([[3], [4], [0]])
	V = np.array([[0], [0], [5]])
	H, N = householder(U, V)

	W = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
	result = matrix_product_left(H, N, W)
	expected = W @ H
	assert_matrix_equal(result, expected, eps)

	W = np.array([[1, 1, 1], [2, 2, 2], [0, 0, 0]])
	result = matrix_product_left(H, N, W)
	expected = W @ H
	assert_matrix_equal(result, expected, eps)

	W = np.array([[0, 0, 0], [2, 2, 2], [3, 3, 3]])
	result = matrix_product_left(H, N, W)
	expected = W @ H
	assert_matrix_equal(result, expected, eps)

	W = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
	result = matrix_product_left(H, N, W)
	expected = W @ H
	assert_matrix_equal(result, expected, eps)

	print("\tOK")


if __name__ == '__main__':
	eps = 1e-7
	test_householder_result(eps)
	test_vector_product_result(eps)
	test_matrix_product_result(eps)
	test_matrix_product_left_result(eps)