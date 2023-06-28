import math as m
from sympy import symbols, Eq

def linear_interpolation(d, x):
    output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
 
    return output
def quadratic_interpolation(d,x):
    pass

# Driver Code
data=[[0.00, 1.35],[1.00, 2.94]]
x=0.73


data2 = [[0,0],[m.radians(30), 0.328],[m.radians(45), 0.560]]


print(m.pow(m.radians(30), 2))

print("{:.2f}".format(linear_interpolation(data, x)))