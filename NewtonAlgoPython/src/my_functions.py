print('__My_Functions loaded.')

def f_281(x = 0) :
    return 32*(4*x**8 - 8*x**6 + 5*x**4 - x**2) + 1

def der_f_281(x = 0) :
    return 64*(16*x**7 - 24*x**5 + 10*x**3 - x)

def f_110(x = 0) :
    return 5*x**3 + 2*x**2 - 15*x - 6

def der_f_110(x = 0) :
    return 15*x**2 + 4*x - 15

def f_111(x = 0) :
    return (1/48)*x**4 + (13/12)*x**3 - (11/4)*x**2 + (9/2)*x - (1/2)

def der_f_111(x = 0) :
    return (1/12)*x**3 + (13/4)*x**2 - (11/2)*x + (9/2)

def f_65536(x=0):
    x**6+101*x**5+425*x**4-425*x**2-101*x-1

def der_f_65536(x=0):
    6*x**5+505*x**4+1700*x**3-850*x-101