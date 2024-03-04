from part4 import compress
from utils import assert_image_near

import matplotlib.pyplot as plt

def test_compression_result(r, eps):
	print(f"Test compression result with rank {r}...", end=" ")

	im = plt.imread('res/part-4.png')
	result = compress(im, r)
	expected_im = plt.imread(f'res/part-4-rank-{r}.png')[:, :, :3] # Removing alpha component
	
	assert_image_near(result, expected_im, eps)
	print("\tOK")


if __name__ == '__main__':
	ranks = (5, 50, 130)
	eps = 0.05
	for r in ranks:
		test_compression_result(r, eps)