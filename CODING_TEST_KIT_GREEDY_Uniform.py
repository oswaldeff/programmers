from collections import Counter
def solution(n, lost, reserve):
    persons = [x for x in range(1, n+1)]
    clothes = {}
    for p in persons:
        clothes[p] = 1
    for p in lost:
        clothes[p] -= 1
    for p in reserve:
        clothes[p] += 1
    for p in persons:
        if p == 1:
            if clothes[p] == 2:
                clothes[p] = 1
                if clothes[p+1] == 0:
                    clothes[p+1] = 1
        if p != 1 and p != len(persons):
            if clothes[p] == 2:
                clothes[p] = 1
                if clothes[p-1] != 0 and clothes[p+1] == 0:
                    clothes[p+1] = 1
                if clothes[p-1] == 0:
                    clothes[p-1] = 1
        if p == len(persons):
            if clothes[p] == 2:
                clothes[p] = 1
                if clothes[p-1] == 0:
                    clothes[p-1] = 1
                
    cnt = Counter(clothes.values())
    answer = cnt[1]
    return answer