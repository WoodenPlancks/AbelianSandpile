import numpy as np
from matplotlib import pyplot as plt

def main():
	n = 324//2

	grid = np.zeros(shape=(n, n))

	for i in range(5832*8):
		add_grain(grid)
		collapse_pile(grid)
	draw_grid(grid)

def collapse_pile(grid, threshold=4):
	inds_to_collapse = np.argwhere(grid > threshold)
	while(inds_to_collapse.shape[0] != 0):
		for ind in inds_to_collapse:
			x, y = ind
			grid[x, y] -= 4
			grid[x + 1, y] += 1
			grid[x - 1, y] += 1
			grid[x, y + 1] += 1
			grid[x, y - 1] += 1
		inds_to_collapse = np.argwhere(grid > threshold)

def draw_grid(grid):
	plt.imshow(grid, cmap="autumn")
	plt.show()

def add_grain(grid):
	x, y = grid.shape
	grid[x//2, y//2] += 1
	return grid





main()
