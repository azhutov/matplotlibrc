# inspired by https://github.com/garrettj403/SciencePlots/blob/master/examples/plot-examples.py
import numpy as np
import matplotlib.pyplot as plt


pparam = dict(xlabel=r'Time ($\mu$s)', ylabel=r'Population $\rho_{gg}$')

x = np.linspace(0, np.pi, 50)


def model(x, omega):
    return np.sin(omega * x) ** 2


# scatter plot
with plt.style.context(['TQT-RAAQS']):
    fix, ax = plt.subplots()
    for omega in [1, 2]:
        ax.scatter(x, model(x, omega), alpha=0.7)
        ax.plot(x, model(x, omega), label=f'$\Omega={omega}$')
        ax.set(**pparam)
        plt.legend()
        plt.savefig("../examples/figures/figure_scatter.png")

# test color palette
with plt.style.context(['TQT-RAAQS']):
    fix, ax = plt.subplots()
    for omega in [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]:
        ax.plot(x, model(x, omega), label=f'$\Omega={omega}$')
        ax.set(**pparam)
        plt.legend()
        plt.savefig("../examples/figures/figure_palette.png")
