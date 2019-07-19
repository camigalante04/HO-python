import numpy as np
import scipy
import matplotlib.pyplot as pp
from pylab import *

#Abrimos el archivo que contiene los datos (dos columnas que corresponden a X y a Y)

with open('tabla.dat','r') as data:
    
    x=[]
    y=[]
    
    for line in data:
        
        p = line.split()
        x.append(float(p[0]))
        y.append(float(p[1]))

#Con esto controle que estuviera leyendo bien los vectores
#print('x=',x)
#print('y=',y)


#Ahora realizo el grafico con los labels y lo guardo en un archivo pdf

plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
#plt.savefig('scatterplot.pdf')
p=np.poly1d(np.polyfit(x,y,1))
xp = np.linspace(1,10,50)
yp = p(xp)
plt.plot(xp,yp,'r-')
plt.show()
