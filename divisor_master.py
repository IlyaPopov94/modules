n = 0
def dels(n):
    dels = []
    for i in range(1, n + 1):
        if n % i == 0:
            dels.append(i)
    return dels

def is_simple(n):
    dels_list = dels(n)
    if (len(dels_list) == 2) == True & ((1 in dels_list) == True) & ((n in dels_list) == True):
        return True
    else:
        return False

def print_dels(n):
    dels_list = dels(n)
    print('Список делителей {}: {}\n'.format(n, dels_list))

def _get_all_sd(divs_list):
    simple_dvrs = []
    for i in range(0, len(divs_list)):
        if is_simple(divs_list[i]):
            simple_dvrs.append(divs_list[i])
    return simple_dvrs
