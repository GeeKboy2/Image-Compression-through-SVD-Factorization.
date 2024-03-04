import numpy as np

def assert_upper_triangular(a, eps=1e-7):
	n, m = a.shape
	for i in range(n):
		for j in range(m):
			if abs(a[i, j]) > eps and (i > j):
				print("ERROR")
				raise ValueError

def assert_orthogonal(a, eps=1e-7):
	n, _ = a.shape
	assert_matrix_equal(np.eye(n), a @ a.T, eps)

def assert_diagonal(a, eps=1e-7):
	n, m = a.shape
	for i in range(n):
		for j in range(m):
			if abs(a[i, j]) > eps and (i != j):
				print("ERROR")
				raise ValueError

def assert_bidiagonal(a, eps=1e-7):
	n, m = a.shape
	for i in range(n):
		for j in range(m):
			in_zone = (i == j) or (i + 1 == j)
			if abs(a[i, j]) > eps and not in_zone:
				print("ERROR")
				raise ValueError

def assert_vector_equal(a, b, eps=1e-7):
	n = len(a)
	for i in range(n):
		if abs(a[i] - b[i]) > eps:
			print("ERROR")
			raise ValueError

def assert_matrix_equal(a, b, eps=1e-7):
	n, m = a.shape
	for i in range(n):
		for j in range(m):
			if abs(a[i, j] - b[i, j]) > eps:
				print("ERROR")
				raise ValueError

def assert_image_near(a, b, eps=1e-7):
	if np.linalg.norm(a - b) / np.linalg.norm(a) > eps:
		print("ERROR")
		raise ValueError