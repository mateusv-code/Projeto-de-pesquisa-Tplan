import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# limites
L = 10
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)
ax.set_zlim(-L, L)

# remover caixa padrão
ax.set_axis_off()

# desenhar eixos (pretos)
ax.plot([-L, L], [0, 0], [0, 0], color='black')
ax.plot([0, 0], [-L, L], [0, 0], color='black')
ax.plot([0, 0], [0, 0], [-L, L], color='black')

# ticks manuais
ticks = range(-10, 11, 5)

for t in ticks:
    # X
    ax.text(t, 0, 0, f'{t}', color='black')
    # Y
    ax.text(0, t, 0, f'{t}', color='black')
    # Z
    ax.text(0, 0, t, f'{t}', color='black')

# rótulos dos eixos
ax.text(L, 0, 0, 'X', color='black', fontsize=12)
ax.text(0, L, 0, 'Y', color='black', fontsize=12)
ax.text(0, 0, L, 'Z', color='black', fontsize=12)

ax.view_init(elev=25, azim=45)

plt.show()
