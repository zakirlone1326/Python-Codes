#Euclidean distance
import numpy as np
a=np.array([1,2])
b=np.array([4,5])
result = a-b
print(np.sqrt(sum((result)**2)))

#manhattan distance

import numpy as np
a= np.array([1,2])
b=np.array([3,4])
print (sum(abs((a-b)**2)))

#using function euclidean
import numpy as np
def euclidean_dist(p,q):
    return (np.sqrt(sum((p-q)**2)))
p= np.array([1,2])
q=np.array([4,5])
print(euclidean_dist(p,q))

#using function manhattan
import numpy as np
def manhattan_dist(p,q):
    return sum(abs(a-b)**2)

p= np.array([1,2])
q= np.array([3,4])
print(manhattan_dist(p,q))