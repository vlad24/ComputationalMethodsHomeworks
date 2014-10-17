from constants import default_parter, newton_epsilon, max_steps_for_newton_algo, super_start_epsilon
from zero_compare import isLessThan0, isMoreThan0, is0
print('__Newton loaded.')

def find_suspicious_start_intervals(F, left_border, right_border):
    intervals = []
    parter = default_parter
    while (not intervals):
        parter = parter * 2
        shift = (right_border - left_border) / (parter)
        left = left_border
        right = left + shift
        #while we have not scanned the whole interval
        while (right <= right_border):
            if (isLessThan0(F(left)) and isLessThan0(F(right)) or isMoreThan0(F(left)) and isMoreThan0(F(right))) :
                # the same sign, continue scanning
                left = right
                right = right + shift
            elif (isLessThan0(F(left)) and isMoreThan0(F(right)) or isMoreThan0(F(left)) and isLessThan0(F(right))) :
                    # different signs
                    intervals.append([left, right])
                    left = right
                    right = right + shift
            else:
                if (is0(F(left))):
                    intervals.append([left, left])
                else:
                    intervals.append([right, right])
                    left = right
                    right = right + shift
    return intervals         

def find_super_start_on_interval(F, left_border, right_border):
    super_start = None
    parter = default_parter
    while (super_start is None):
        point = left_border
        parter = parter * 2
        shift = (right_border - left_border) / (parter)
        while (point <= right_border):
            F_value = abs(F(point))
            if (F_value < super_start_epsilon) : 
                super_start = point
                return super_start
            else:
                point = point + shift

def find_root_on_suspicious_interval(F, derF, left_border, right_border):
    print('!!! Finding root on the interval (', left_border, ', ', right_border, ').')
    super_start = find_super_start_on_interval(F, left_border, right_border)
    print("Strat point on that interval = ", super_start)
    print('k   |         x[k]        |      F(x[k])       ')
    print("------------------------------------------------")
    k = 0
    current = super_start
    previous = current + newton_epsilon + 1
    while (k < max_steps_for_newton_algo):
        if (abs(current - previous) > newton_epsilon): 
            F_current = F(current)
            derF_current = derF(current)
            print(k,  '|' ,  current,  '|',   F_current)
            previous = current
            current = current - F_current/derF_current
            k += 1
            #moving towards the root
        else :
            print(k,  '|' ,  current,  '|',   F(current))
            print('! Root found on ', k, ' step', current)
            return current
    #unlucky
    print('! After ', k, ' steps root has not been found.')
    return None
    
def find_roots(F, derF, left_border, right_border):
    print('****************************')
    start_intervals = find_suspicious_start_intervals(F, left_border, right_border)
    print("Suspicious intervals", start_intervals)
    roots = []
    for interval in start_intervals:
        roots.append(find_root_on_suspicious_interval(F, derF, interval[0], interval[1]))
    return roots

def print_roots(roots):
    print('--------------------------\nApproximate roots found:')
    k = 0
    for root in roots:
        k += 1
        print(k,'.   ', root)
    print('--------------------------')
