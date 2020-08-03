import numpy as np
import matplotlib.pyplot as plt
def area_trap_way(a,b,n):
    #assuming func is y=2x^2
    dx=(b-a)/n
    area=0
    for i in np.arange(a,b+dx,dx):
        area+=0.5*dx*((2*(i**2))+(2*((i+dx)**2)))
    return area
def error_check(a,b,n):
    actual_res=4+(2/3)
    error=actual_res-area_trap_way(a,b,n)
    return abs(error*100)
z=[100,250,500,750,1000]
a=[1 for x in z]
b=[2 for x in z]
Z=list(map(error_check,a,b,z))
plt.plot(z,Z,'b.')
plt.xlabel("# of Steps")
plt.ylabel("Percent Error for Trapezoid Method")
plt.title("Error for func 2x^2 using Trapezoid Method")
plt.show()
