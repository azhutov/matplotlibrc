import numpy as np

WIDTH = 246  # width of the figure
FACTOR = 1  # the fraction of the width you'd like the figure to occupy
fig_width_pt = WIDTH * FACTOR

inches_per_pt = 1.0 / 72.27
golden_ratio = (np.sqrt(5) - 1.0) / 2.0

fig_width_in = fig_width_pt * inches_per_pt  # figure width in inches
fig_height_in = fig_width_in * golden_ratio   # figure height in inches
fig_dims = [fig_width_in, fig_height_in]  # fig dims as a list
print(f'[fig_width_in, fig_height_in]=[{fig_dims[0]:0.4f}, {fig_dims[1]:0.4f}]')
