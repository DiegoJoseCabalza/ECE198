import numpy as np
import skfuzzy as fuzz
x = np.arange(11)
mfx = fuzz.trimf(x, [0, 5, 10])
print(x)
print(mfx)
