import time
from collections import defaultdict
from itertools import combinations
def binary_search(m_index, scores, p_scores, q_score):
    print("-----------")
    print("next m_index: ", m_index)
    if q_score == scores[m_index]:
        print("binary q_score: ", q_score)
        scores = scores[m_index:]
        print("binary scores: ", scores)
        p_scores = p_scores[m_index:]
        print("binary p_scores: ", p_scores)
        return p_scores
    elif q_score > scores[m_index]:
        pass
    elif q_score < scores[m_index]:
        m_index = m_index-1
        return binary_search(m_index, scores, p_scores, q_score)
def solution(info, query):
    start_time = time.time()
    persons = list(range(len(info)))
    applicants_group = {}
    scores = []
    scores_group = defaultdict(list)
    for idx, i in enumerate(info):
        applicant_info = i.split(" ")[0:4]
        applicant_score = i.split(" ")[-1]
        applicants_group[idx] = {}
        applicants_group[idx]['info'] = []
        applicants_group[idx]['score'] = int(applicant_score)
        scores.append(int(applicant_score))
        scores_group[int(applicant_score)].append(idx)
        for j in range(1, len(applicant_info)+1):
            comb = list(map("".join, combinations(applicant_info, j)))
            applicants_group[idx]['info'].extend(comb)
    scores = sorted(scores)
    print("applicants_group: ", applicants_group)
    print("scores: ", scores)
    print("scores_group: ", scores_group)
    p_scores = []
    for score in scores:
        p_scores.append(scores_group[score].pop())
    print("p_scores: ", p_scores)
    # m_index
    mean_score = int(sum(scores)/len(scores))
    m_index = 0
    for idx, score in enumerate(scores):
        if score >= mean_score:
            m_index = idx
            break
    print("First m_index: ", m_index)
    answer = []
    for q in query:
        q = q.replace(" and ", " ")
        q = q.split(" ")
        q_info = q[0:4]
        q_info = "".join(q_info)
        q_info = q_info.replace("-", "")
        q_score = int(q[-1])
        #p_scores = binary_search(m_index, scores, p_scores, q_score)
        #print("Result p_scores: ", p_scores)
        passers = []
        for person in persons:
            pass
        answer.append(len(passers))
    end_time = time.time()
    print(end_time - start_time)
    return answer
# first trial: 0.00013303756713867188
if solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]) == [1, 1, 1, 1, 2, 4]:
    print("test case result: correct")
else:
    print("test case result: incorrect")

