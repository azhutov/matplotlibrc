
# Template for figures


Matplotlib styles for publication-quality plots


# Installation

Clone this repository by running the following command in a terminal

```sh
git clone https://github.com/azhutov/matplotlibrc
```

Then move `.mplstyle` files from `matplotlibrc/styles` folder to `mpl_configdir/stylelib` (you might need to create this directory), where `mpl_configdir` is given by `matplotlib.get_configdir()`. On Linux, the config directory for matplotlib is `~/.config/matplotlib`. For detailed explanations use [[1](https://github.com/azhutov/matplotlibrc#resources)].

Finally, install Roboto font from <https://fonts.google.com/specimen/Roboto>.

# Usage

```python
import matplotlib.pyplot as plt

# set global style
plt.style.use('TQT-RAAQS')

plt.plot(x, y)

# or temporarly set style (textwidth style sets figure site to the two column width)
with plt.style.context(['TQT-RAAQS', 'textwidth']):
    plt.figure()
    plt.plot(x, y)
```

# Example plots

* Scatter plot

<img src="https://github.com/azhutov/matplotlibrc/blob/master/examples/figures/figure_scatter.png?raw=true" width="500">

* Test color palette

<img src="https://github.com/azhutov/matplotlibrc/blob/master/examples/figures/figure_palette.png?raw=true" width="500">

# Resources

-   [1] [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
-   [2] [SciencePlots](https://github.com/garrettj403/SciencePlots)
