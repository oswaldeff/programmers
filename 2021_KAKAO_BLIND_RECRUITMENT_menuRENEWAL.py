from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    comb_l = defaultdict(list)
    for idx_s, order in enumerate(orders):
        order_list = list(order)
        for idx_l in range(2, len(order_list)):
            element = list(map(''.join, combinations(order_list, idx_l)))
            comb_l[idx_l].extend(element)
    print('comb_l: ', comb_l)
    
    
    comb_c = defaultdict(list)
    for c in course:
        comb_c[c] = set(comb_l[c])
    print('comb_c: ', comb_c)
    
    answer = []
    return answer