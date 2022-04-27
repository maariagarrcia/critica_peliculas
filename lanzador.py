from fileinput import filename
import math
import csv
import numpy as np
class calculos:

    filename = 'critica_pelicula.csv' 

    with open(filename) as f:
        
        # Crear objeto iterable
        header = next(f)

        # Imprimir 1era fila.
        for h in header:
            print(h, end='')

    def percentiles():
        # Calcular percentiles sin el csv 
        # Se calcula con listas
        cantidad_valoraciones = np.array([42,96,132,124,88,58])
        p = np.percentile(cantidad_valoraciones,68) 
        print ("El percentil es", p)

calculos.percentiles()


                

