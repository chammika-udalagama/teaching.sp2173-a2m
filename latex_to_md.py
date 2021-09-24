import numpy as np
import matplotlib.style
import matplotlib.pyplot as plt
import pyperclip
import re

# %%

s = pyperclip.paste()
# s = r'''\item \textbf{Frequency}  and \textbf{Wave Height}  are useful measures of the \textbf{energy} contained in a wave.
# \item \textbf{Wavelength} is the most useful measure of wave size.'''


pattern = [[r'\\textbf\{(.*?)\}', r'**\1**']]
pattern += [[r'\\texttt\{(.*?)\}', r'`\1`']]
pattern += [[r'\\answer.*\{(.*?)\}', r'`r fill("\1")`']]
pattern += [[r'\\section\*?\{(.*?)\}', r'## \1']]
pattern += [[r'\\underline\{(.*?)\}', r'<u>\1</u>']]


rep = {r'\item ': '*\t',
       r'\scriptsize': '',
       r'\begin{equation}': '$$',
       r'\end{equation}': '$$'
       }

for p in pattern:
    s = re.sub(p[0], p[1], s)

for k in rep.keys():
    s = s.replace(k, rep[k])

pyperclip.copy(s)
print(s)

# %%
s = pyperclip.paste()
# s = f'`r me.t("{s}")`'
s = f'`r hi("{s.upper()}")`'
pyperclip.copy(s)
print(s)


# %%
s = pyperclip.paste()
s = f'`r me.t("{s}")`'
pyperclip.copy(s)
print(s)

# %%
s = pyperclip.paste()
s = f'`r hi("{s.upper()}")`'
pyperclip.copy(s)
print(s)


# %%
# matplotlib.style.use('bmh')

x = np.linspace(0, 4*pi, 1000)

a = pi/2
b = 3

plt.plot(x, np.sin(x), label='A')
plt.plot(x, np.sin(x+a), label='B')
plt.plot(x, b+np.sin(x+a)+np.sin(x), c='g', label='A+B')
plt.legend(loc=1)
plt.axis('off')
plt.grid()
plt.show()

# %%


def l(x=-0, off=0):
    return (-.5+x, -1+off)


pi = np.pi
a = pi/2
b = -3
colors = ['k', 'red', 'g', 'b', 'y']
color_cnt = -1
offset = -b


plt.figure(figsize=(10, 8))

x = np.linspace(0, 6*pi, 1000)
lines = np.arange(-1, 9, 2)*pi/2
plt.vlines(lines, 4*b, 2, linestyles='--', colors='k', alpha='.2')
plt.hlines(b*np.arange(4), -2*pi, 4*pi, linestyles='--', colors='k', alpha='.05')

plt.vlines(0, 4*b, 2, linestyles='-', colors='k', alpha='.1')
# 1
color_cnt += 1
offset += b
print(offset)
plt.plot(x, offset+np.sin(x), color=colors[color_cnt])
plt.text(*l(off=offset), f'$S_1$', fontsize=15, color=colors[color_cnt])

# 2
color_cnt += 1
offset += b
plt.plot(x, offset+np.sin(x), color=colors[color_cnt])
plt.text(*l(off=offset), f'$S_2$\n$(\Delta = 0)$', fontsize=15, color=colors[color_cnt], ha='center')

# 3
color_cnt += 1
offset += b
X = x - pi
plt.plot(X, offset+np.sin(x), color=colors[color_cnt])
plt.text(*l(x=X[0], off=offset), f'$S_3$\n($\Delta = \lambda/2)$', fontsize=15, color=colors[color_cnt], ha='center')

# 4
color_cnt += 1
offset += b
X = x - 2*pi
plt.plot(X, offset+np.sin(x), color=colors[color_cnt])
plt.text(*l(x=X[0], off=offset), f'$S_4$\n($\Delta = \lambda$)', fontsize=15, color=colors[color_cnt], ha='center')

# 5
color_cnt += 1
offset += b
X = x - pi/2
plt.plot(X, offset+np.sin(x), color=colors[color_cnt])
plt.text(*l(x=X[0], off=offset), f'$S_5$\n($\Delta = \lambda/4$)', fontsize=15, color=colors[color_cnt], ha='center')

pos = np.arange(0, 5*pi, pi/2)
labels = []
for i in range(len(pos)):
    if i == 0:
        labels.append(0)
    elif i % 2 == 0:
        labels.append(f'{int(i*1/2)}$\lambda$')
    else:
        labels.append('$\dfrac{\lambda}{2}$'.replace('\lambda', f'{i}\lambda'))
# labels = [j.replace('\lambda',f'{i}\lambda') for i,j in enumerate(labels) if i%2==0]

plt.xticks(pos, labels, fontsize=20)
plt.yticks([])
plt.xlim(-2*pi, 4*pi)
# plt.grid()
plt.box(on=None)
plt.savefig('a2m_waves-phase.png', dpi=300)
plt.show()
