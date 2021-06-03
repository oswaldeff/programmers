from collections import defaultdict
from itertools import combinations
def solution(info, query):
    persons = list(range(len(info)))
    print(persons)
    applicants_group = defaultdict(list)
    for idx, i in enumerate(info):
        applicant_info = i.split(" ")
        for j in range(len(applicant_info)):
            comb = list(map("".join, combinations(applicant_info, j)))
            applicants_group[idx].extend(comb)
    print(applicants_group)
    
    answer = []
    for q in query:
        q = q.replace(" and ", " ")
        q = q.replace(" ", "")
        q = q.replace("-", "")
        passers = []
        for person in persons:
            print('person: ', person)
            if q in applicants_group[person]:
                passers.append(person)
        answer.append(len(passers))
    return answer

if solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]) == [1, 1, 1, 1, 2, 4]:
    print("test case result: correct")
else:
    print("test case result: incorrect")

