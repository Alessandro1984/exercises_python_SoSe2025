import math
import numpy as np

x = [1, 10, 100, 1000, 10000, 100000, 
     1000000, 10000000, 100000000, 
     1000000000, 10000000000]

x_log = []

for wert in x:
    x_log.append(math.log10(wert))
    
print(x_log)

x_array_log = np.log10(x)

print(x_array_log)