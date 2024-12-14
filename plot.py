import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def plot_filled_circle(ax, center, radius, plane='xy', color='blue', alpha=0.5):
    """
    Plots a filled 2D circle in a 3D space on a given plane.
    """
    theta = np.linspace(0, 2 * np.pi, 100)  # Parametric angle for the circle
    if plane == 'xy':
        x = center[0] + radius * np.cos(theta)
        y = center[1] + radius * np.sin(theta)
        z = np.full_like(x, center[2])  # z is constant
    elif plane == 'xz':
        x = center[0] + radius * np.cos(theta)
        y = np.full_like(x, center[1])  # y is constant
        z = center[2] + radius * np.sin(theta)
    elif plane == 'yz':
        x = np.full_like(theta, center[0])  # x is constant
        y = center[1] + radius * np.cos(theta)
        z = center[2] + radius * np.sin(theta)
    else:
        raise ValueError("Invalid plane. Use 'xy', 'xz', or 'yz'.")
    
    # Create a filled polygon for the circle
    vertices = np.array([x, y, z]).T  # Transpose to get (x, y, z) vertices
    poly = Poly3DCollection([vertices], color=color, alpha=alpha)
    ax.add_collection3d(poly)

def plot_3d_box(ax, position, size, face_color='purple', edge_color='purple', alpha=0.5):
    """
    Plots a 3D rectangular box (rectangular prism) with pastel-like transparency and edges.
    """
    x, y, z = position
    sx, sy, sz = size

    # Define the vertices of the box
    vertices = np.array([
        [x, y, z],  # Bottom face
        [x + sx, y, z],
        [x + sx, y + sy, z],
        [x, y + sy, z],
        [x, y, z + sz],  # Top face
        [x + sx, y, z + sz],
        [x + sx, y + sy, z + sz],
        [x, y + sy, z + sz]
    ])

    # Define the six faces of the box
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back
        [vertices[3], vertices[0], vertices[4], vertices[7]],  # Left
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top
        [vertices[0], vertices[1], vertices[2], vertices[3]]   # Bottom
    ]

    # Add the faces to the plot with transparency
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

# Create the 3D figure
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')

# Set the figure background to dark gray
fig.patch.set_facecolor('#2b2b2b')  # Dark gray background

# Set the axes background to a slightly lighter dark gray
ax.set_facecolor('#383838')  # Slightly lighter dark gray

# Change grid and tick colors to light for visibility
ax.xaxis._axinfo['grid']['color'] = (1, 1, 1, 0.2)  # Light grid
ax.yaxis._axinfo['grid']['color'] = (1, 1, 1, 0.2)
ax.zaxis._axinfo['grid']['color'] = (1, 1, 1, 0.2)

# Set axis labels color to white
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.zaxis.label.set_color('white')

# Set axis tick labels (numbers) to white
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')

# Define circle properties
radius = 2  # All circles have the same radius
z_position = 0  # All circles lie on Z = 0

# Place centers for slight separation
center_blue = (-1.2, 0.2, z_position)  # Moved slightly up and left
center_green = (1.2, 0.2, z_position)  # Moved slightly up and right
center_red = (0, -1.8, z_position)     # Moved slightly down

# Plot filled circles
plot_filled_circle(ax, center=center_blue, radius=radius, plane='xy', color='lightblue', alpha=0.5)  # Blue circle
plot_filled_circle(ax, center=center_green, radius=radius, plane='xy', color='lightgreen', alpha=0.5)  # Green circle
plot_filled_circle(ax, center=center_red, radius=radius, plane='xy', color='lightcoral', alpha=0.5)  # Red circle

# Add the 3D purple box at z = 2
box_position = (-3, 2, 2)  # Bottom-left-front corner of the box
box_size = (1, 1, 1)  # Dimensions of the box (width, depth, height)
plot_3d_box(ax, position=box_position, size=box_size, face_color='violet', edge_color='purple', alpha=0.5)

# Annotate intersections
ax.text(0, -2.8, 0.3, "S_0", color='red', fontsize=12, weight='bold')
ax.text(2, 0, 0.3, "A_0", color='green', fontsize=12, weight='bold')
ax.text(-2, 0, 0.3, "M_0", color='blue', fontsize=12, weight='bold')
ax.text(0, -1.1, 0.3, "M ∩ A ∩ S", color='black', fontsize=12, weight='bold')
ax.text(0, 0.50, 0.3, "M ∩ A", color='black', fontsize=12, weight='bold')
ax.text(-1.1, -1.3, 0.3, "S ∩ M", color='black', fontsize=12, weight='bold')
ax.text(1, -1.2, 0.3, "A ∩ S", color='black', fontsize=12, weight='bold')

# Annotate the purple box
ax.text(-2.8, 2.2, 2.7, "E", color='purple', fontsize=12, weight='bold')

# Set camera rotation
ax.view_init(elev=48, azim=-31)

# Ensure circles are round by setting equal aspect ratio
set_equal_aspect_3d(ax)

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Save the plot
plt.savefig('taxonomy.png', dpi=300, bbox_inches='tight')
ax.view_init(elev=90, azim=0)
plt.savefig('overview.png', dpi=300, bbox_inches='tight')
plt.show()
