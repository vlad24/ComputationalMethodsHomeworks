import root_estimator
from my_functions import *
from newton import find_roots, print_roots

if __name__ == '__main__':
    print("32*(4*x^8 - 8*x^6 + 5*x^4 - x^2) + 1")
    polyList_281 = [128,0,-256,0,160,0,-32,0,1]
    root_limits_281 = root_estimator.get_limits_dict(polyList_281)
    print(root_limits_281) 
    roots_281 = find_roots(f_281, der_f_281, root_limits_281['negative_down'], root_limits_281['positive_up'])
    print_roots(roots_281)
    print("####################################")
    print("5*x^3 + 2*x^2 - 15*x - 6")
    polyList_110 = [5,2,-15,-6]
    root_limits_110 = root_estimator.get_limits_dict(polyList_110)  
    print(root_limits_110)   
    roots_110 = find_roots(f_110, der_f_110, root_limits_110['negative_down'], root_limits_110['positive_up'])
    print_roots(roots_110)
    print("####################################")
    polyList_111 = [1/48,13/12,-11/4, 9/2, -1/2]
    root_limits_111 = root_estimator.get_limits_dict(polyList_111)
    print(root_limits_111)     
    roots_111 = find_roots(f_111, der_f_111, root_limits_111['negative_down'], root_limits_111['positive_up'])
    print_roots(roots_111)
#     print("####################################")
#     print("x**6+101*x**5+425*x**4-425*x**2-101*x-1")
#     polyList_65536 = [1, 101, 425, 0, -425, -101, -1]
#     root_limits_65536 = root_estimator.get_limits_dict(polyList_65536)
#     print(root_limits_65536)     
#     roots_65536 = find_roots(f_65536, der_f_65536, root_limits_65536['negative_down'], root_limits_65536['positive_up'])
#     print_roots(roots_65536)