import numpy as np
print(np.zeros((208,21)))
print('\n')
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

array = np.random.random(10)
print(array)
print('\n')
value = float(input())
print(find_nearest(array, value))
