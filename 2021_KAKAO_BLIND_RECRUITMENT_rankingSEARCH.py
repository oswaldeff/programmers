# def solution(info, query):
#     applicants_graph = {}
#     for idx, i in enumerate(info):
#         applicants_graph[idx] = {}
#         applicants_graph[idx]["language"] = i.split(" ")[0]
#         applicants_graph[idx]["position"] = i.split(" ")[1]
#         applicants_graph[idx]["career"] = i.split(" ")[2]
#         applicants_graph[idx]["soulfood"] = i.split(" ")[3]
#         applicants_graph[idx]["score"] = i.split(" ")[4]
        
#     answer = []
#     for q in query:
#         applicants = [x for x in range(len(info))]
#         passers = []
#         data = (q.replace(" and ", " ")).split(" ")
#         while applicants:
#             applicant = applicants.pop(0)
#             if data[0] != '-' and applicants_graph[applicant]["language"] != data[0]:
#                 continue
#             if data[1] != '-' and applicants_graph[applicant]["position"] != data[1]:
#                 continue
#             if data[2] != '-' and applicants_graph[applicant]["career"] != data[2]:
#                 continue
#             if data[3] != '-' and applicants_graph[applicant]["soulfood"] != data[3]:
#                 continue
#             if int(applicants_graph[applicant]["score"]) < int(data[4]):
#                 continue
#             else:
#                 passers.append(applicant)
#         answer.append(len(passers))
#     return answer

from collections import defaultdict
def solution(info, query):
    classification_graph = defaultdict(list)
    classification_graph['-'] = [x for x in range(len(info))]
    for idx, i in enumerate(info):
        classification_graph[i.split(" ")[0]].append(idx)
        classification_graph[i.split(" ")[1]].append(idx)
        classification_graph[i.split(" ")[2]].append(idx)
        classification_graph[i.split(" ")[3]].append(idx)
        classification_graph[idx].append(i.split(" ")[4])
    #print(classification_graph)
    applicants = []
    answer = []
    for q in query:
        passers = []
        data = (q.replace(" and ", " ")).split(" ")
        #language: data[0]
        #position: data[1]
        #career: data[2]
        #soulfood: data[3]
        #score: data[4]
        if data[0] != '-':
            applicants.extend(classification_graph[data[0]])
        if data[0] == '-':
            if data[1] != '-':
                applicants.extend(classification_graph[data[1]])
            if data[1] == '-':
                if data[2] != '-':
                    applicants.extend(classification_graph[data[2]])
                if data[2] == '-':
                    if data[3] != '-':
                        applicants.extend(classification_graph[data[3]])
                    if data[3] == '-':
                        applicants.extend(classification_graph['-'])
        while applicants:
            applicant = applicants.pop(0)
            if data[1] != '-' and applicant not in classification_graph[data[1]]:
                continue
            if data[2] != '-' and applicant not in classification_graph[data[2]]:
                continue
            if data[3] != '-' and applicant not in classification_graph[data[3]]:
                continue
            if int(classification_graph[applicant][0]) < int(data[4]):
                continue
            else:
                passers.append(applicant)
        answer.append(len(passers))
    return answer

if solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]) == [1, 1, 1, 1, 2, 4]:
    print("test case result: correct")
else:
    print("test case result: incorrect")

