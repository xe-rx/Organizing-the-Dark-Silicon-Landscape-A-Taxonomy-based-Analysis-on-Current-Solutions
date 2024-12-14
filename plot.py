import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def plot_filled_circle(ax, center, radius, plane='xy', color='blue', alpha=0.5):
    """
    Plots a filled 2D circle in a 3D space on a given plane.
    """
    theta = np.linspace(0, 2 * np.pi, 100)
    if plane == 'xy':
        x = center[0] + radius * np.cos(theta)
        y = center[1] + radius * np.sin(theta)
        z = np.full_like(x, center[2])
    elif plane == 'xz':
        x = center[0] + radius * np.cos(theta)
        y = np.full_like(x, center[1])
        z = center[2] + radius * np.sin(theta)
    elif plane == 'yz':
        x = np.full_like(theta, center[0])
        y = center[1] + radius * np.cos(theta)
        z = center[2] + radius * np.sin(theta)
    else:
        raise ValueError("Invalid plane. Use 'xy', 'xz', or 'yz'.")
    

    vertices = np.array([x, y, z]).T
    poly = Poly3DCollection([vertices], color=color, alpha=alpha)
    ax.add_collection3d(poly)

def plot_3d_box(ax, position, size, face_color='purple', edge_color='purple', alpha=0.5):
    """
    Plots a 3D rectangular box (rectangular prism) with pastel-like transparency and edges.
    """
    x, y, z = position
    sx, sy, sz = size


    vertices = np.array([
        [x, y, z],
        [x + sx, y, z],
        [x + sx, y + sy, z],
        [x, y + sy, z],
        [x, y, z + sz],
        [x + sx, y, z + sz],
        [x + sx, y + sy, z + sz],
        [x, y + sy, z + sz]
    ])

 
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[1], vertices[2], vertices[6], vertices[5]], 
        [vertices[2], vertices[3], vertices[7], vertices[6]], 
        [vertices[3], vertices[0], vertices[4], vertices[7]], 
        [vertices[4], vertices[5], vertices[6], vertices[7]], 
        [vertices[0], vertices[1], vertices[2], vertices[3]] 
    ]


    poly = Poly3DCollection(faces, facecolor=face_color, edgecolor=edge_color, alpha=alpha, linewidths=1)
    ax.add_collection3d(poly)

def set_equal_aspect_3d(ax):
    """
    Sets equal aspect ratio for a 3D plot.
    """
    extents = np.array([getattr(ax, f'get_{dim}lim')() for dim in 'xyz'])
    centers = np.mean(extents, axis=1)
    radius = 0.5 * np.max(extents[:, 1] - extents[:, 0])
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, f'set_{dim}lim')(ctr - radius, ctr + radius)


fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')


fig.patch.set_facecolor('#2b2b2b') 


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


radius = 2
z_position = 0 


center_blue = (-1.2, 0.2, z_position)
center_green = (1.2, 0.2, z_position)
center_red = (0, -1.8, z_position)  


plot_filled_circle(ax, center=center_blue, radius=radius, plane='xy', color='lightblue', alpha=0.5)  # Blue circle
plot_filled_circle(ax, center=center_green, radius=radius, plane='xy', color='lightgreen', alpha=0.5)  # Green circle
plot_filled_circle(ax, center=center_red, radius=radius, plane='xy', color='lightcoral', alpha=0.5)  # Red circle


box_position = (-3, 2, 2)
box_size = (1, 1, 1) 
plot_3d_box(ax, position=box_position, size=box_size, face_color='violet', edge_color='purple', alpha=0.5)


ax.text(0, -2.8, 0.3, "S_0", color='red', fontsize=12, weight='bold')
ax.text(2, 0, 0.3, "A_0", color='green', fontsize=12, weight='bold')
ax.text(-2, 0, 0.3, "M_0", color='blue', fontsize=12, weight='bold')
ax.text(0, -1.1, 0.3, "M ∩ A ∩ S", color='black', fontsize=12, weight='bold')
ax.text(0, 0.50, 0.3, "M ∩ A", color='black', fontsize=12, weight='bold')
ax.text(-1.1, -1.3, 0.3, "S ∩ M", color='black', fontsize=12, weight='bold')
ax.text(1, -1.2, 0.3, "A ∩ S", color='black', fontsize=12, weight='bold')


ax.text(-2.8, 2.2, 2.7, "E", color='purple', fontsize=12, weight='bold')


ax.view_init(elev=48, azim=-31)


set_equal_aspect_3d(ax)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.savefig('taxonomy.png', dpi=300, bbox_inches='tight')
ax.view_init(elev=90, azim=0)
plt.savefig('overview.png', dpi=300, bbox_inches='tight')
plt.show()
