from part3 import SVD

import numpy as np

def reduced_svd(array, r):
	"""
	Returns an array with values removed in its SVD decomposition
	"""
	n = min(len(array), len(array[0]))

	#u, s, v = SVD(array, 20)
	u, s, v = np.linalg.svd(array)
	res = np.zeros(array.shape)
	res[:n, :n] = np.diag(s)
	
	for k in range(r, n):
		res[k, k] = 0
	return u @ res @ v


def compress(img, r):
	"""
	Returns a (n, m, 3) image, compressed at rank r using the SVD method
	"""
	n, m, _ = img.shape

	red = green = blue = np.zeros((n, m))
	red = img[:, :, 0]
	green = img[:, :, 1]
	blue = img[:, :, 2]

	new_red = reduced_svd(red, r)
	new_blue = reduced_svd(blue, r)
	new_green = reduced_svd(green, r)

	red_im = np.zeros(img.shape)
	green_im = np.zeros(img.shape)
	blue_im = np.zeros(img.shape)

	red_im[:, :, 0] += new_red
	green_im[:, :, 1] += new_green
	blue_im[:, :, 2] += new_blue

	new_im = red_im + blue_im + green_im

	# May need to change
	new_im[new_im > 1.] = 1.
	new_im[new_im < 0.] = 0.
	
	return new_im


def image_dist(im1, im2):
	return np.linalg.norm(im1 - im2) / np.linalg.norm(im1)


if __name__ == '__main__':
	import matplotlib.pyplot as plt

	nmax = 300

	# Making sure the compress function works correctly
	ranks = (5, 20)
	im = plt.imread('res/part-4.png')
	n, m, _ = im.shape
	
	plt.figure(figsize=(15, 5))

	plt.subplot(1, 3, 1)
	plt.title(f"Compression SVD de rang {ranks[0]}")
	new_im = compress(im, ranks[0])
	plt.imshow(new_im)

	plt.subplot(1, 3, 2)
	plt.title(f"Compression SVD de rang {ranks[1]}")
	new_im = compress(im, ranks[1])
	plt.imshow(new_im)

	plt.subplot(1, 3, 3)
	plt.title(f"Image originale")
	plt.imshow(im)

	plt.tight_layout()
	plt.show()

	# Drawing distance between the default file and compressed ones
	x = [k for k in range(0, nmax + 1, 4)]
	
	y = [image_dist(im, compress(im, r)) for r in x]

	rlim = n * m / (n + m)

	plt.plot(x, y)
	plt.axvline(x = rlim, color = 'r', label = '$r_{lim}$')
	
	plt.title("Tracé de la distance à l'image originale\nen fonction du rang de compression")
	plt.xlabel("Rang de la compression")
	plt.ylabel("Distance euclidienne à l'image originale")
	plt.yscale('log')
	plt.grid()
	plt.legend()

	plt.tight_layout()
	plt.show()

	# Drawing file size depending on compression rank
	x = [k for k in range(nmax + 1)]
	y = [3 * k * (n + m) for k in range(nmax + 1)]

	plt.plot(x, y, label='Taille compressée')
	plt.plot([0, nmax], [3 * n * m, 3 * n * m], color='r', label='Taille originale')
	
	plt.title("Taille du fichier\n en fonction du rang de compression")
	plt.xlabel("Rang de la compression")
	plt.ylabel("Taille du fichier en nombre de données")
	plt.grid()
	plt.legend()

	plt.tight_layout()
	plt.show()
