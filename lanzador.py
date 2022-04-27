import math
import csv
import numpy as np
import math
import functools
def percentiles():
   # Calcular percentiles sin el csv 
   # Se calcula con listas
   cantidad_valoraciones = np.array([42,96,132,124,88,58])
   p = np.percentile(cantidad_valoraciones,68) 
   print ("El percentil es", p)

percentiles()

import numpy as np

b = np.array([42,96,132,124,88,58])
print('percentiles using default interpolation')
p68 = np.percentile(b, 68) 
p95 = np.percentile(b, 95) 
p97 = np.percentile(b, 97) 
print('p10 = ',p68,', median = ',p95,' and p90 = ',p97)
