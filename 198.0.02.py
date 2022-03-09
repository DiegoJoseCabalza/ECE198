import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#####
## try repeat test3 but for dimensions, particles, velocity, and position

# Generate universe variables
# * Quality and service on subjective ranges [0, 10]
x_dimension = np.arange(0, 10, 1)
x_particle = np.arange(0, 10, 1)
x_velocity = np.arange(0, 10, 1)
x_position = np.arange(0, 10, 1)


# Generate fuzzy membership functions
dim_lo = fuzz.trimf(x_dimension, [0, 0, 5])
dim_hi = fuzz.trimf(x_dimension, [5, 10, 10])
part_lo = fuzz.trimf(x_particle, [0, 0, 5])
part_hi = fuzz.trimf(x_particle, [5, 10, 10])
vel_lo = fuzz.trimf(x_velocity, [0, 0, 5])
vel_hi = fuzz.trimf(x_velocity, [5, 10, 10])
pos_lo = fuzz.trimf(x_position, [0, 0, 5])
pos_hi = fuzz.trimf(x_position, [5, 10, 10])

#based from testcode, cant show plot for whatever reason
#attempts in printing the output
fig, (ax0) = plt.subplots(nrows=3, figsize=(8, 9))
ax0.plot(x_dimension, dim_lo, linewidth=1.5, label='A')
ax0.plot(x_dimension, dim_md, linewidth=1.5, label='B')
ax0.set_title('dimension')
ax0.legend()
print(dim_lo)


