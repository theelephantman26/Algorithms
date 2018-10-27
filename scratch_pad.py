import numpy as np

a = [-1, -1, 1]
(values, counts) = np.unique(a,return_counts=True)
ind=np.argmax(counts)
print(values[ind])
