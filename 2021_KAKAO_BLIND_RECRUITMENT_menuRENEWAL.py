from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    comb = defaultdict(list)
    for idx_s, order in enumerate(orders):
        order_list = list(order)
        for idx_l in range(2, len(order_list)):
            comb[idx_s].extend(list(combinations(order_list, idx_l)))
    print(comb)
    answer = []
    return answer