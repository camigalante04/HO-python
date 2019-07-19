import numpy as np
import matplotlib.pyplot as pp
from scipy import optimize as opt

p = np.poly1d([1,1,-4,4])
dp = np.polyder(p)
#Como la salida del paso anterior es un 
roots = np.roots(dp.coef)

#print(dp)
#print(roots)

xp = np.arange(-10,10,0.1)
yp = p(xp)

xdp = np.arange(-10,10,0.1)
ydp = dp(xdp)

xr1 = roots[0]
yr1 = p(xr1)

#print(xr1,yr1)

xr2 = roots[1]
yr2 = p(xr2)

#print(xr2,yr2)

data = np.array([xp,yp])
data = data.T

open('salida.dat','w+')
np.savetxt('salida.dat',data,fmt=['%.2f','%.2f'])

pp.grid(True)
pp.xlim(-10.,10.)
pp.ylim(-10.,10.)
pp.xlabel('X')
pp.ylabel('Y')
pp.plot(xp,yp,'m-',label='polinomio')
pp.plot(xdp,ydp,'c--',label='derivada')
pp.plot(xr1,yr1,'ko')
pp.plot(xr2,yr2,'ko',label='extremos')
pp.legend()
#pp.show()
#pp.savefig('grafico-pol.pdf')


