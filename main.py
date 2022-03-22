import numpy as np
from matplotlib import pyplot as plt


def simulate_sandpile(n=90, num_grains=5832, cmap="Inferno"):
	grid = np.zeros(shape=(n, n))

	for i in range(num_grains):
		add_grain(grid)
		collapse_pile(grid)
	draw_grid(grid, cmap)

	return grid


def collapse_pile(grid, threshold=4):
	inds_to_collapse = np.argwhere(grid > threshold)
	while (inds_to_collapse.shape[0] != 0):
		for ind in inds_to_collapse:
			x, y = ind
			grid[x, y] -= 4
			grid[x + 1, y] += 1
			grid[x - 1, y] += 1
			grid[x, y + 1] += 1
			grid[x, y - 1] += 1
		inds_to_collapse = np.argwhere(grid > threshold)


def draw_grid(grid, grid_cmap):
	plt.imshow(grid, cmap=grid_cmap)
	plt.show()


def add_grain(grid):
	x, y = grid.shape
	grid[x // 2, y // 2] += 1
	return grid
