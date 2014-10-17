import math
print('__My_Functions loaded.')

def f(k, x, y) :
    return math.exp(k * x + y) - x*y - 1.4 

def g(a, x, y) :
    return (x**2)/(a**2) + 2*(y**2) - 4

def der_f_x(k, x, y) :
    return k * math.exp(k * x + y) - y 

def der_f_y(k, x, y) :
    return math.exp(k * x + y) - x

def der_g_x(a, x, y) :
    return 2* x/(a**2)

def der_g_y(a, x, y) :
    return 4 * y

def det_x(a, k, x, y):
    return der_f_y(k, x, y) * g(a,x,y) - der_g_y(a, x, y) * f(k, x, y)
    
def det_y(a, k, x, y):
    return der_g_x(a, x, y) * f(k,x,y) - g(a, x, y) * der_f_x(k, x, y)
    
def det(a, k, x, y):
    return der_f_x(k, x, y) * der_g_y(a, x, y) - der_f_y(k, x, y) * der_g_x(a, x, y)