# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:50:29 2015
@author: FIFA
Aplicación del ajuste lineal sobre un conjunto sintetico de datos para ilustrar el ajuste de cuadrados minimos
https://github.com/fifabsas/talleresfifabsas/blob/master/python/3_Aplicaciones_basicas/Ajuste_lineal/Ajuste_lineal.py

"""

#==============================================================================
# IMPORTACIÓN DE LAS BIBLIOTECAS QUE NECESITAMOS USAR
#==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

#==============================================================================
# IMPORTACIÓN DE LOS DATOS DESDE UN ARCHIVO DE EXCEL
#==============================================================================

xls_file = pd.ExcelFile('dato.xls') # Importar el archivo de Excel de esta dirección

df = xls_file.parse('Sheet1') # En particular los datos de esta hoja

data = np.array(df) # Guardo en la variable data los datos que importé, en forma de array (es como una matriz)

x1 = data[:,0] # guardo en la variable x todos los datos de la columna 0

y1 = data[:,1] # guardo en la variable y todos los datos de la columna 1

yerr1 = data[:,2] # guardo en la variable yerr todos los datos de la columna 2
         
#==============================================================================
# Grafico datos
#==============================================================================

plt.errorbar(x1,y1,yerr1,fmt= 'o')
plt.show()

#==============================================================================
#Aplicar funcion para Linealizar modelo
#==============================================================================
           
x = x1
xlab = 'x [unidades de x]'

y = y1
ylab = 'y [unidades de y]'
yerr = yerr1


#==============================================================================
# Elimina numeros indefinidos provocados por la funcion
#==============================================================================
x=np.nan_to_num(x)
y=np.nan_to_num(y)
yerr=np.nan_to_num(yerr)
#==============================================================================
# Ajustes lineales
#==============================================================================

f = lambda x, B, M: M * x + B # la función modelo, con la que ajustamos

print('Ajuste lineal')
popt, pcov = curve_fit(f, x, y)#ajusto sin incertezas en y
sigmas = np.sqrt([pcov[0,0],pcov[1,1]])# las incertezas de los parametros son la raiz de la diagonal de la matriz de covarianza
b=popt[0]
m=popt[1]
eb=sigmas[0]
em=sigmas[1]
print('Ordenada al origen: ' + str(b) + ' ± ' + str(eb))
print('Pendiente ' + str(m) + ' ± ' + str(em))
print('')

print('Ajuste lineal con incertezas en y')
popt, pcov = curve_fit(f, x, y, sigma = yerr,absolute_sigma=True)#ajusto con incertezas en y
                #sigma son las incertezas en y. absolute_sigma para que las considere absolutas.
sigmas = np.sqrt([pcov[0,0],pcov[1,1]])# las incertezas de los parametros son la raiz de la diagonal de la matriz de covarianza
b=popt[0]
m=popt[1]
eb=sigmas[0]
em=sigmas[1]
print('Ordenada al origen: ' + str(b) + ' ± ' + str(eb))
print('Pendiente ' + str(m) + ' ± ' + str(em))


# graficamos
plt.errorbar(x,y,yerr=yerr,fmt='o')#,10000,fmt='-o',color='g')
plt.plot(x,m*x+b,'r')#,10000,fmt='-o',color='g')
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title('Ajuste con incertezas en y')
plt.legend(("Ajuste","Datos"), loc=4)
plt.grid('on')#para que muestre la grilla
