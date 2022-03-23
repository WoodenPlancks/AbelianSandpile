import numpy as np
from matplotlib import pyplot as plt

class LoadingBar():
	def __init__(self):
		self.percent_done = 0

loading_bar = LoadingBar()

def simulate_sandpile(window, n=90, num_grains=5832):
	grid = np.zeros(shape=(n, n))
	grains_done = 0

	for i in range(num_grains):
		add_grain(grid)
		collapse_pile(grid)
		grains_done += 1
		loading_bar.percent_done = grains_done/num_grains*100
		window["progress_bar"].update_bar(loading_bar.percent_done)

	return grid


def collapse_pile(grid, threshold=4):
	inds_to_collapse = np.argwhere(grid > threshold)
	while (inds_to_collapse.shape[0] != 0):
		for ind in inds_to_collapse:
			x, y = ind
			grid[x, y] -= 4
			if x + 1 < grid.shape[0]:
				grid[x + 1, y] += 1
			if x - 1 >= 0:
				grid[x - 1, y] += 1
			if y + 1 < grid.shape[1]:
				grid[x, y + 1] += 1
			if y - 1 >= 0:
				grid[x, y - 1] += 1
		inds_to_collapse = np.argwhere(grid > threshold)


def draw_grid(grid, grid_cmap):
	plt.imshow(grid, cmap=grid_cmap)
	plt.axis('off')
	plt.show()


def add_grain(grid):
	x, y = grid.shape
	grid[x // 2, y // 2] += 1
	return grid
