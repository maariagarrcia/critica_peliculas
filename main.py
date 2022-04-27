
import pandas as pnd
import peliculas as jmp
import numpy as np

#--- CREACION DE UN DATAFRAME ----
observaciones = pnd.DataFrame({'Cantidad de votantes':np.array([42,96,132,124,88,58])})

#--- ANALISIS DE UNA CARACTERISTICA ---
stats = jmp.JMPEstadisticas(observaciones['votaciones'])
stats.analisisCaracteristica()