import literal_copy as lc

import numpy as np

#a = lc.syntax_like(np.array([[5,4,3], [1,2,1]], dtype=np.uint8)).print()
#print(a)

a = lc.syntax_like(np.array([["Hello", "World"], ['Bluh', 'Blub']])).print()
print(a)