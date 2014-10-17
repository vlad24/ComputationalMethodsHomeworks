import copy

print('root_estimator loaded')

def is_valid_polynom(x=[]) :
    return x[0] > 0

def minus_polynom(newPolynom = []):
    for i in range(len(newPolynom)):
                newPolynom[i] = -newPolynom[i] 

def minus_variable_substitute(coefs=[]) :
    for i in range(len(coefs) - 1):
        if (i % 2 != 0) :
            coefs[i] = -coefs[i]
    
def reverse_variable_substitute(coefs=[]) :
    coefs.reverse()

def estimate_positive_up(polynom=[]) :
    if is_valid_polynom(polynom) :
        minCoef = min(polynom)
        firstCoef = polynom[0]
        rootDegree = 1/polynom.index(minCoef)
        return 1 + (abs(minCoef)/firstCoef)**(rootDegree)
    else :
        newPolynom = copy.deepcopy(polynom)
        minus_polynom(newPolynom)
        minCoef = min(newPolynom)
        firstCoef = newPolynom[0]
        rootDegree = 1/newPolynom.index(minCoef)
        return 1 + (abs(minCoef)/firstCoef)**(rootDegree)
    
def estimate_positive_down(polynom=[]) :
        newPolynom = copy.deepcopy(polynom)
        reverse_variable_substitute(newPolynom)
        return 1/estimate_positive_up(newPolynom)

def estimate_negative_down(polynom=[]) :
        newPolynom = copy.deepcopy(polynom)
        minus_variable_substitute(newPolynom)
        return -estimate_positive_up(newPolynom)
    
def estimate_negative_up(polynom=[]) :
        newPolynom = copy.deepcopy(polynom)
        minus_variable_substitute(newPolynom)
        reverse_variable_substitute(newPolynom)
        return 1/(-estimate_positive_up(newPolynom))
    
def get_limits_dict(polynom=[]):
    diction = {}
    diction['positive_up'] = estimate_positive_up(polynom)
    diction['positive_down'] = estimate_positive_down(polynom)
    diction['negative_up'] = estimate_negative_up(polynom)
    diction['negative_down'] = estimate_negative_down(polynom)
    return diction
        