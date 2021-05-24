from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    comb_list = []
    for idx_s, order in enumerate(orders):
        order_list = sorted(list(order))
        for idx_l in range(2, len(order_list)+2):
            element = list(map(''.join, combinations(order_list, idx_l)))
            comb_list.extend(element)
    comb_list = sorted(comb_list)
    comb_list = sorted(comb_list, key=len)
    print('comb_list: ', comb_list)
    comb_set = sorted(list(set(comb_list)))
    comb_set = sorted(comb_set, key=len)
    print('comb_set: ', comb_set)
    comb_dict = defaultdict(int)
    cnt = 0
    for comb1 in comb_set:
        for comb2 in comb_list:
            if comb1 == comb2:
                comb_dict[comb1] += 1
    print('comb_dict: ', comb_dict)
    
    answer = []
    return answer