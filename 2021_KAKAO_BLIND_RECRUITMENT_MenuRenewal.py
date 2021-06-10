from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    comb_list = []
    for idx_s, order in enumerate(orders):
        order_list = sorted(list(order))
        for idx_l in range(2, len(order_list)+2):
            element = list(map(''.join, combinations(order_list, idx_l)))
            comb_list.extend(element)
    # sort
    comb_list = sorted(comb_list)
    comb_list = sorted(comb_list, key=len)
    comb_set = sorted(list(set(comb_list)))
    comb_set = sorted(comb_set, key=len)
    # combination dictionary 
    comb_dict = {}
    for c in course:
        comb_dict[c] = defaultdict(lambda:0)
    
    for comb1 in comb_set:
        for comb2 in comb_list:
            if comb1 == comb2:
                if len(comb1) in list(comb_dict.keys()):
                    comb_dict[len(comb1)][comb1] += 1
    # answer
    answer = []
    for c in course:
        if list(comb_dict[c].values()) != []:
            max_val = max(list(comb_dict[c].values()))
            if max_val > 1:
                for idx, val in enumerate(list(comb_dict[c].values())):
                    if max_val == val:
                        answer.append(list(comb_dict[c].keys())[idx])
    answer = sorted(answer, reverse=False)
    
    return answer
