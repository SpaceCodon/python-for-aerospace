import math
import numpy as np
import matplotlib.pyplot as plt

# Define data for planets
planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
semi_major_axis = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.22, 30.05]  # in AU (astronomical units)
orbit_period = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]  # in years

plt.style.use('dark_background')
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

# Plot the Sun at the center
ax.scatter(0,0, color="yellow", s=75, label="Sun")

# Plot orbits of planets
for i, planet in enumerate(planet_names):
    orbital_radius = semi_major_axis[i]
    orbit_theta = np.linspace(0,2*math.pi,100)
    x = orbital_radius * np.cos(orbit_theta)
    y = orbital_radius * np.sin(orbit_theta)
    z = np.zeros_like(x)

    ax.plot(x, y, z, label=planet)

ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title("Simplified 3D solar system")
ax.legend()

plt.show()