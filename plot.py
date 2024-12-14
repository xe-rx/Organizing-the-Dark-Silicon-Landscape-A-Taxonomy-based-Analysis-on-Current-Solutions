"""
University of Amsterdam
Bachelor, Computer Science
By
Marouan Bellari & Boris Vukajlovic
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches

def plot_box(ax, position, sizes, color, alpha=0.5):
    x, y, z = position
    sx, sy, sz = sizes

    vertices = [
        [x,      y,      z],
        [x+sx,   y,      z],
        [x+sx,   y+sy,   z],
        [x,      y+sy,   z],
        [x,      y,      z+sz],
        [x+sx,   y,      z+sz],
        [x+sx,   y+sy,   z+sz],
        [x,      y+sy,   z+sz]
    ]

    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  
        [vertices[1], vertices[2], vertices[6], vertices[5]],  
        [vertices[2], vertices[3], vertices[7], vertices[6]],  
        [vertices[3], vertices[0], vertices[4], vertices[7]],  
        [vertices[4], vertices[5], vertices[6], vertices[7]],  
        [vertices[0], vertices[1], vertices[2], vertices[3]]   
    ]

    ax.add_collection3d(Poly3DCollection(faces, color=color, alpha=alpha))

fig = plt.figure(figsize=(12, 12))

fig.patch.set_facecolor('#383838')

ax = fig.add_subplot(111, projection='3d')

ax.set_facecolor('#383838')

ax.xaxis._axinfo['grid']['color'] = (1, 1, 1, 0.2)
ax.yaxis._axinfo['grid']['color'] = (1, 1, 1, 0.2)
ax.zaxis._axinfo['grid']['color'] = (1, 1, 1, 0.2)

ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.zaxis.label.set_color('white')

ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')

blue_cube = (-2, -2, -0.5, 3.5, 3, 1)
green_cube = (-0.75, -0.75, 0.2, 2, 2, 0.8)
red_cube = (-0.5, -1.6, 0.2, 1.5, 1.8, 0.6)

plot_box(ax, blue_cube[:3], blue_cube[3:], 'lightblue', 0.2)
plot_box(ax, green_cube[:3], green_cube[3:], 'lightgreen', 0.2)
plot_box(ax, red_cube[:3], red_cube[3:], 'lightcoral', 0.2)

ax.text(0, -0.5, 0.4, "M ∩ A ∩ S", color='black', fontsize=12, weight='bold')
ax.text(0, 0.50, 0.4, "M ∩ A", color='blue', fontsize=12, weight='bold')
ax.text(0, -1.4, 0.4, "S ∩ M", color='red', fontsize=12, weight='bold')
ax.text(0, -0.55, 0.65, "A ∩ S", color='green', fontsize=12, weight='bold')

blue_patch = mpatches.Patch(color='lightblue', label='M')
green_patch = mpatches.Patch(color='lightgreen', label='A')
red_patch = mpatches.Patch(color='lightcoral', label='S')
plt.legend(handles=[blue_patch, green_patch, red_patch], loc='upper left', fontsize=12)

ax.set_box_aspect([1, 1, 1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=11, azim=-8)
plt.savefig('taxonomy.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())

plt.show()
