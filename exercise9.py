import numpy as np

a = np.arange(1, 13)

a_reshaped = a.reshape(3, 2, 2)

print(a_reshaped.ndim)
print(a_reshaped.size)
print(a_reshaped.size)
print(a_reshaped.dtype)
