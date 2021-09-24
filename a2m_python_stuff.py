from sympy import *
import itertools
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

max_number_of_terms = 1500
no_x_pts = 1000

c = [calculate_c(n) for n in range(1, max_number_of_terms+1, 2)]
x = np.linspace(start=0, stop=1, num=no_x_pts, endpoint=True)


def calculate_c(n):
    v = n*np.pi/4
    c = (np.cos(v)-np.cos(3*v))
    c *= np.sqrt(2)/(n*np.pi)

    return c


def f(x):
    return (x >= .25) & (x <= .75)


def psi(x, n):
    return np.sqrt(2)*np.sin(n*np.pi*x)


def sum(x, no_of_terms):
    sum = np.zeros(shape=len(x))
    for c_index, n in enumerate(range(1, no_of_terms+1, 2)):
        sum = sum + c[c_index]*np.sqrt(2)*np.sin(n*np.pi*x)
    return sum


# Miss out the even numbers
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.left'] = False

# %%
y0 = f(x)
plt.plot(x, y0)
plt.fill_between(x, y0, 0, color='gray', alpha=.15)
plt.gca().set_aspect(.25)
plt.savefig('./my-figures/a2m_python_square.png',  transparent=True, bb_box_inch='tight', pad_inch=0)

# %%
set_of_n = {'a': [1, 5, 10],
            'b': [1, 5, 10, 25, 50, 75, 100, 250, 500, 1000]
            }

set_of_n = set_of_n['b']


# plt.style.use('bmh')
no_of_rows = len(set_of_n)

# plt.clf()
_, ax = plt.subplots(nrows=no_of_rows, ncols=1,
                     sharex=True, figsize=(10, no_of_rows*2.5))

y0 = f(x)

for plot_index, no_of_terms in enumerate(set_of_n, start=0):
    a = ax[plot_index]
    a.plot(x, y0, color='gray')
    a.fill_between(x, y0, 0, color='gray', alpha=.05)

    y = sum(x, no_of_terms)
    a.plot(x, y, color='orange')
    a.fill_between(x, y, 0, color='orange', alpha=.05)

    _ = a.text(.5, .2, f'Using {no_of_terms} Terms',
               ha='center', fontdict={'fontsize': 20, 'color': (.3, 0, 0)})

    a.set_aspect(.25)
    a.set_ylim(-.25, 1.25)
    a.set_xlim(0, 1)
    a.axes.get_yaxis().set_visible(False)

    # b = ax[plot_index, 1]
    #
    # for n in range(1, no_of_terms+1, 2):
    #     b.plot(x, psi(x, n))

# for a in ax.flat:
#     a.set_xlim(0, 1)

plt.tight_layout()
plt.savefig('./my-figures/a2m_python_complete.png', dpi=150, transparent=True, bb_box_inch='tight', pad_inch=0)


# %%
plt.clf()
style = itertools.cycle(['solid', 'dashed', 'dashdot', 'dotted'])
_, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

for n in range(1, 5+1):
    ax[0].plot(x, psi(x, n), color='k', alpha=.7, linestyle=next(style), label=f'$c_{n} \psi_{n}$')

ax[1].plot(x, y0, label='Original function', alpha=.5)
ax[1].fill_between(x, y0, 0, color='gray', alpha=.05)
ax[1].plot(x, sum(x, 5), label='Sum with 5 terms')

for a in ax:
    a.get_yaxis().set_visible(False)
    a.set_aspect(.25)
    a.set_xlim(0, 1)
    a.set_ylim(-1.5, 1.5)
    a.legend()

plt.savefig('./my-figures/a2m_python_complete_one-term.png', dpi=150, transparent=True, bb_box_inch='tight', pad_inch=0)

# %%
init_printing()
r, t, p = symbols('r \\theta \\phi')
R = symbols('R')

integrate(r, (r, 0, R), (t, 0, 2*pi))
integrate(r**2*sin(t), (r, 0, R), (t, 0, pi), (p, 0, 2*pi))
