import numpy as np
import matplotlib.pyplot as plt
import spiceypy as spice

# Reading SPICE files
spice.furnsh("./kernels/cassMetaK.txt")

step = 4000
UTC = ["Jun 20, 2004", "Dec 1, 2005"]
etOne = spice.str2et(UTC[0])
etTwo = spice.str2et(UTC[1])
print(f"Ephemeris Time 1: {etOne}, Ephemeris Time 2: {etTwo}")

# Calculate time range
times = [x*(etTwo-etOne)/step + etOne for x in range(step)]

positions, lightTimes = spice.spkpos("Cassini", times, "J2000", "NONE", "SATURN BARYCENTER")
spice.kclear()

# Plotting trajectory
positions = np.asarray(positions).T
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection="3d")
ax.plot(positions[0], positions[1], positions[2])
plt.title("Cassini Positioning Visualization")
plt.show()