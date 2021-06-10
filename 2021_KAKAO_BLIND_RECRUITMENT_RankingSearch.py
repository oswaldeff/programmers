from collections import defaultdict
from itertools import combinations
def b_search(passers, q_score):
    start_idx = 0
    end_idx = len(passers)
    while (start_idx != end_idx) and (start_idx != len(passers)):
        quotient = (start_idx+end_idx)//2
        if passers[quotient] >= q_score:
            end_idx = quotient
        else:
            start_idx = quotient+1
    cnt = len(passers)-start_idx
    return cnt

def solution(info, query):
    # Making db
    scores = []
    applicants_db = defaultdict(list)
    for idx, i in enumerate(info):
        applicants_info = i.split(" ")[0:4]
        applicants_score = int(i.split(" ")[-1])
        scores.append(applicants_score)
        for j in range(1, len(applicants_info)+1):
            comb = list(map("".join, combinations(applicants_info, j)))
            for c in comb:
                applicants_db[c].append(applicants_score)
    # Sorting @sort in "for", couldn't pass efficiency test
    scores = sorted(scores)
    for val in applicants_db.values():
        val.sort()
    # Searching passers
    answer = []
    for q in query:
        passers = []
        q = q.replace(" and ", " ")
        q = q.split(" ")
        q_info = q[0:4]
        q_info = "".join(q_info)
        q_info = q_info.replace("-", "")
        q_score = int(q[-1])
        if len(applicants_db[q_info]) > 0:
            passers = applicants_db[q_info]
            cnt = b_search(passers, q_score)
        else:
            if q_info == "":
                passers = scores
                cnt = b_search(passers, q_score)
            else:
                cnt = 0
        answer.append(cnt)
    
    return answer
