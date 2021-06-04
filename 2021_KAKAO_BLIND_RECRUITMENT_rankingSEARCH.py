import time
from collections import defaultdict
from itertools import combinations
def solution(info, query):
    start_time = time.time()
    persons = list(range(len(info)))
    applicants_group = {}
    for idx, i in enumerate(info):
        applicant_info = i.split(" ")[0:4]
        applicant_score = i.split(" ")[-1]
        applicants_group[idx] = {}
        applicants_group[idx]['info'] = []
        for j in range(1, len(applicant_info)+1):
            comb = list(map("".join, combinations(applicant_info, j)))
            applicants_group[idx]['info'].extend(comb)
            applicants_group[idx]['score'] = int(applicant_score)
    #print("applicants_group: ", applicants_group)
    
    answer = []
    for q in query:
        q = q.replace(" and ", " ")
        q = q.split(" ")
        q_info = q[0:4]
        q_info = "".join(q_info)
        q_info = q_info.replace("-", "")
        q_score = int(q[-1])
        passers = []
        for person in persons:
            # print("applicants_group[person]['info']: ", applicants_group[person]['info'])
            # print("applicants_group[person]['score']: ", applicants_group[person]['score'])
            # print("q_info: ", q_info)
            # print("q_score: ", q_score)
            if q_info != '':
                if q_info in applicants_group[person]['info'] and applicants_group[person]['score'] >= q_score:
                    passers.append(person)
            if q_info == '':
                if applicants_group[person]['score'] >= q_score:
                    passers.append(person)
        answer.append(len(passers))
    end_time = time.time()
    print(end_time - start_time)
    return answer

if solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]) == [1, 1, 1, 1, 2, 4]:
    print("test case result: correct")
else:
    print("test case result: incorrect")

