import math
import csv
import numpy as np

def percentiles():
   # Calcular percentiles sin el csv 
   # Se calcula con listas
   cantidad_valoraciones = np.array([42,96,132,124,88,58])
   p = np.percentile(cantidad_valoraciones,68) 
   print ("El percentil es", p)

percentiles()


                

